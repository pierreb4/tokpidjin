# Scoring System Documentation

## Overview

The scoring system evaluates solver quality through two mechanisms:
1. **O_Score**: Direct output matching (perfect match = 1000 points)
2. **D_Score**: Improvement measurement via differs (baseline vs solver performance)

The system prevents output leakage through a two-pass evaluation strategy.

## Core Components

### The batt() Function

The `batt()` function produces two lists:

- **List `o`**: Solver outputs as tuples `(t_n, evo, solver_id, output)`
- **List `s`**: Differ scores as tuples `(last_t, solver_id, differ_name, score_tuple)`

Note: Original solvers may be mutated during batt() function construction.

### Two-Pass Anti-Leakage Strategy

We call `batt()` twice per sample with different parameters:

**Pass 1: Output Generation** - `batt(task_id, S, I, I, pile_log_path)`
- Uses input `I` for both input and expected output parameters
- Produces solver outputs in list `o` (no output leakage)
- Differ scores in list `s` are not meaningful (both inputs are the same)

**Pass 2: Differ Evaluation** - `batt(task_id, S, I, O, pile_log_path)`
- Uses actual output `O` for differ evaluation
- List `o` contains outputs (but we don't use them to avoid leakage)
- List `s` contains meaningful differ scores (measuring quality improvements)

**Why Two Passes?**
- We want solver outputs generated WITHOUT seeing the actual output `O`
- We want differ scores calculated WITH the actual output `O` for accurate measurement
- This prevents solvers from "cheating" by accessing the expected output

## Baseline Measurement

Differs are first run with `solver_id='None'` to establish a baseline quality score.

**How It Works:**
1. Differ runs on input `I` without any solver transformation → produces baseline score (0-1000)
2. Same differ runs after solver processes `I` → produces solver score (0-1000)
3. Improvement = `solver_score - baseline_score`

**Example:**
- Baseline score: 300 (differ rates untransformed input as low quality)
- Solver score: 700 (differ rates solver output as higher quality)
- **Improvement: 700 - 300 = 400 points**

## Scoring Classes

### O_Score (Solver Correctness)
```python
class O_Score:
    score = {
        'solver_id_1': 1000,  # One perfect match
        'solver_id_2': 2000,  # Two perfect matches
    }
```
- Tracks perfect output matches (C == O)
- Each perfect match adds 1000 points
- Used in Phases 1-3 for solver selection

### D_Score (Differ-Based Improvement)
```python
class D_Score:
    score = {
        'solver_id_1': {
            'differ_name_1': {
                'last_t': 42,      # Terminal operation from baseline
                'score': 400       # Cumulative improvement (solver - baseline)
            },
            'differ_name_2': {...}
        }
    }
    
    last_t = {
        'differ_name_1': 42,  # Stored when solver_id == 'None' (baseline)
    }
```

**D_Score.update() Logic:**
```python
def update(self, solver_id, s_item):
    last_t, s_solver_id, d_name, return_tuple = s_item
    sample_score = return_tuple[0]  # 0-1000 range
    
    # When processing baseline ('None'), SUBTRACT the baseline score
    if s_solver_id == 'None':
        self.score[solver_id][d_name]['score'] += -sample_score  # e.g., -300
        self.last_t[d_name] = last_t  # Store for differ generation
    
    # When processing solver, ADD the solver score
    if s_solver_id == solver_id:
        self.score[solver_id][d_name]['score'] += sample_score  # e.g., +700
    
    # Net result: 700 - 300 = 400 improvement
```

**D_Score.get() Logic:**
```python
def get(self, solver_id):
    # Sum all differ improvements for this solver
    total = sum(self.score[solver_id][d_name]['score'] 
                for d_name in self.score[solver_id])
    
    # Clamp to 0 (solver worse than baseline = 0, not negative)
    return max(0, total)
```

### S_Score (Differ-Centric View)
```python
s_score = {
    'differ_name_1': S_Score(),  # One S_Score per differ
    'differ_name_2': S_Score()
}

class S_Score:
    score = {
        'solver_id_1': 400,  # Copied from D_Score
        'solver_id_2': -100  # Negative = solver worse than baseline
    }
```
- Built from D_Score after aggregation completes
- Provides differ-centric view (vs D_Score's solver-centric view)
- Used in Phase 4 for differ selection

## Score Values and Ranges

### Per-Sample Scores
- Differ scores: **0-1000** (clamped at source)
- Perfect match: **1000** (from eval_match)
- Imperfect match: Uses differ_score from D_Score.get()

### Accumulated Scores (Per Task)
- **D_Score per solver per differ**: Can be positive (improvement) or negative (regression)
  - Example: 10 samples × 400 improvement = **4000 total**
- **D_Score.get() result**: Clamped to **[0, ∞)** (sum of all differs, minimum 0)
- **O_Score per solver**: Multiple of 1000 (number of perfect matches)
  - Example: 3 perfect matches = **3000**

### Global Scores (Across All Tasks)
- **tot_d_score**: Sum of all differ improvements across all tasks and solvers
- Accumulates only from non-timeout tasks

## Complete Scoring Pipeline

### 1. Sample Processing (score_sample)
**Location:** `run_batt.py` lines 900-965

```python
def score_sample(args):
    # Unpack arguments
    task_id, S, I, O, sample_type, i, d_score, ...
    
    # PASS 1: Generate outputs (no O leakage)
    sample_o, sample_s = batt(task_id, S, I, I, pile_log_path)
    
    # PASS 2: Evaluate differs (with actual O)
    _, sample_s_result = batt(task_id, S, I, O, pile_log_path)
    sample_s.extend(sample_s_result)
    
    # Optional: Print matches for debugging
    for t_n, evo, o_solver_id, okt in sample_o:
        if okt == O:
            print_l(f'- MATCH: {o_solver_id}')
    
    return {
        'outputs': sample_o,
        'solver_scores': sample_s,
        ...
    }
```

**Key Point:** D_Score is NOT updated here (removed duplicate update).

### 2. Result Aggregation (_aggregate_sample_results)
**Location:** `run_batt.py` lines 752-828

```python
def _aggregate_sample_results(results, task, sample_type, all_o, 
                               o_score, d_score, s_score, S, prof=None):
    
    for result in results:
        # Update D_Score from differ results (SINGLE UPDATE LOCATION)
        for s_item in result['solver_scores']:
            o_solver_id = s_item[1]
            d_score.update(o_solver_id, s_item)  # Line 807
        
        # Evaluate outputs with accumulated differ scores
        for t_n, evo, o_solver_id, okt in result['outputs']:
            differ_score = d_score.get(o_solver_id)  # Line 812
            _, score = eval_match(S, okt, O, differ_score)  # Line 813
            o_score.update(o_solver_id, score)  # Line 814
    
    # Build S_Score from D_Score (after all samples processed)
    for solver_id in d_score.score:
        for d_name in d_score.score[solver_id]:
            if d_name not in s_score:
                s_score[d_name] = S_Score()
            s_score[d_name].update(solver_id, 
                d_score.score[solver_id][d_name]['score'])
    
    return o, s, all_o
```

**Key Points:**
- D_Score updated ONCE per s_item (fixed duplicate bug)
- eval_match called AFTER all differ scores accumulated
- S_Score built immediately after aggregation completes

### 3. Task Orchestration (check_batt)
**Location:** `run_batt.py` lines 990-1150

```python
async def check_batt(task_id, S, demo_task, test_task, ...):
    o_score = O_Score()
    s_score = {}  # Dict of S_Score instances
    
    # Process ALL samples (demo + test) in parallel
    all_sample_args = [...]  # Combined demo + test samples
    results = await process_samples_parallel(all_sample_args)
    
    # Aggregate demo results
    o['demo'], s['demo'], all_o = _aggregate_sample_results(
        demo_results, demo_task, 'demo', all_o, 
        o_score, d_score, s_score, S, prof
    )
    
    # Aggregate test results
    o['test'], s['test'], all_o = _aggregate_sample_results(
        test_results, test_task, 'test', all_o,
        o_score, d_score, s_score, S, prof
    )
    
    return all_o, o_score, s_score
```

### 4. Global Aggregation (main loop)
**Location:** `run_batt.py` lines 2085-2093

```python
tot_d_score = 0
for task_i, task_id in enumerate(do_list):
    d_score = D_Score()  # NEW instance per task
    timed_out, ret_d_score = await run_batt(task_id, d_score, ...)
    
    if not timed_out:
        # Accumulate differ scores across all tasks
        for solver_id in ret_d_score.score:
            for d_name in ret_d_score.score[solver_id]:
                tot_d_score += ret_d_score.score[solver_id][d_name]["score"]
```

**Key Point:** Each task gets a NEW D_Score instance, then scores accumulated globally.

## eval_match Function

**Location:** `run_test.py` line 80

```python
def eval_match(S, C, O, differ_score=0):
    perfect_match = (C == O)
    
    if C is None or O is None:
        return perfect_match, 0
    
    if perfect_match:
        return perfect_match, 1000  # Perfect match gets 1000
    else:
        return perfect_match, differ_score  # Use differ improvement score
```

**Key Points:**
- Perfect match: Always returns 1000 (ignores differ_score)
- Imperfect match: Returns differ_score from D_Score.get()
- differ_score is already clamped to [0, ∞) by D_Score.get()

## Aggregation Strategy

### Per-Sample Aggregation
- Differ scores from multiple differs accumulated in D_Score
- Formula: `total = solver_score - baseline_score` per differ
- Multiple differs can contribute to same solver

### Per-Task Aggregation
- D_Score accumulates across all samples (demo + test)
- Example: 5 demo + 5 test samples = 10 score updates per differ
- S_Score built from final D_Score state

### Cross-Task Aggregation
- Each task has independent D_Score instance
- Global `tot_d_score` sums all improvements across all tasks
- Used for overall performance metrics

## Data Flow Summary

```
score_sample() [PARALLEL PER SAMPLE]
├─> batt(I, I) → outputs (no leakage)
├─> batt(I, O) → differ scores
└─> Return: outputs + differ scores

_aggregate_sample_results() [PER TASK]
├─> D_Score.update() for all solver_scores (ONCE)
├─> D_Score.get() → differ_score
├─> eval_match(C, O, differ_score) → final_score
├─> O_Score.update(final_score)
└─> S_Score built from D_Score

check_batt() [PER TASK]
├─> Process demo samples → aggregate
├─> Process test samples → aggregate
└─> Return: all_o, o_score, s_score

main() [GLOBAL]
├─> For each task: NEW D_Score
├─> run_batt() → ret_d_score
└─> Accumulate to tot_d_score
```

## Fixed Bugs (Nov 2025)

### Bug 1: Incorrect Normalization Formula ✅ FIXED
**Before:** `score += (1000 - baseline) + solver` → 1400 for baseline=300, solver=700  
**After:** `score += -baseline + solver` → 400 for baseline=300, solver=700  
**Location:** `run_batt.py` line 884

### Bug 2: Double D_Score Update ✅ FIXED
**Before:** D_Score.update() called in both `score_sample()` line 947 AND `_aggregate_sample_results()` line 807  
**After:** Single update in `_aggregate_sample_results()` only  
**Impact:** Scores were doubled (2x inflation)

### Bug 3: Premature eval_match ✅ FIXED
**Before:** eval_match called in `score_sample()` with incomplete differ scores  
**After:** eval_match called only in `_aggregate_sample_results()` after all scores accumulated  
**Location:** Removed from `score_sample()` lines 950-957

### Bug 4: Negative Score Handling ✅ FIXED
**Before:** D_Score.get() could return negative values when solver worse than baseline  
**After:** Added `max(0, sum(...))` to clamp to 0  
**Location:** `run_batt.py` line 894

### Bug 5: S_Score Consolidation Delayed ✅ FIXED
**Before:** S_Score built in separate loop after aggregation (lines 1153-1157)  
**After:** S_Score built during aggregation immediately after D_Score finalized  
**Impact:** Better code organization and performance

## Usage

### Phase 1-3: Solver Selection
```python
# Use O_Score to find best solvers
best_score = o_score.get(solver_id)
if best_score >= threshold:
    keep_solver(solver_id)
```

### Phase 4: Differ Selection
```python
# Use S_Score to find best differs
for differ_name, s_score_instance in s_score.items():
    differ_quality = s_score_instance.get(solver_id)
    if differ_quality >= threshold:
        keep_differ(differ_name, solver_id)
```

### Global Metrics
```python
print(f'Total improvement across all tasks: {tot_d_score}')
```
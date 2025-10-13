# Week 4 Day 1-2: Implementation Plan

## 🎯 Goal
Modify card.py to generate `batt_vectorized()` - a GPU-friendly batch version without try/except

## 📋 Tasks

### Task 1: Add Command-Line Flag (30 min)
- [x] Add `--vectorized` flag to argparse
- [x] Pass flag through to main() and Code class

### Task 2: Modify Code Class (2 hours)
- [ ] Add `vectorized` mode to Code.__init__()
- [ ] Modify mutate() to skip try/except in vectorized mode
- [ ] Generate pre-validation code instead of try/except
- [ ] Track operation types for batch processing

### Task 3: Generate Batch-Friendly Batt (3 hours)
- [ ] Modify main() to generate batt_vectorized() signature
- [ ] Change function signature to accept batch inputs
- [ ] Generate type validation at start
- [ ] Generate batch operations where possible
- [ ] Return success flags with results

### Task 4: Create Validation Helpers (2 hours)
- [ ] Generate _validate_batch_types() function
- [ ] Generate _handle_batch_failures() function
- [ ] Generate batch result merging logic

### Task 5: Test Generation (2 hours)
- [ ] Generate both versions (batt + batt_vectorized)
- [ ] Compare outputs for correctness
- [ ] Verify structure is GPU-friendly

## 📝 Implementation Details

### Changes to card.py

#### 1. Add Flag
```python
parser.add_argument("--vectorized", action="store_true",
                    help="Generate vectorized batch-friendly version")
```

#### 2. Modify Code.mutate()
```python
def mutate(self, is_solver, freeze=False, vectorized=False):
    # ... existing code ...
    
    if vectorized:
        # No try/except - generate validation instead
        print(f'    t{self.t_num} = {call_string}', file=self.file)
    else:
        # Current try/except approach
        print(f'    try:', file=self.file)
        print(f'        t{self.t_num} = {call_string}', file=self.file)
        print(f'    except (TypeError, AttributeError, ValueError):', file=self.file)
        print(f'        t{self.t_num} = _get_safe_default({func_name})', file=self.file)
```

#### 3. Generate Vectorized Signature
```python
if vectorized:
    print(f"def batt_vectorized(inputs_batch):", file=batt_file)
    print(f"    '''Vectorized batch-friendly version for GPU processing'''", file=batt_file)
    print(f"    batch_size = len(inputs_batch)", file=batt_file)
    print(f"    results = []", file=batt_file)
    print(f"    ", file=batt_file)
    print(f"    for task_id, S, I, C in inputs_batch:", file=batt_file)
else:
    # Current signature
    print(f"def batt(task_id, S, I, C, log_path):", file=batt_file)
```

## 🧪 Testing Plan

### Test 1: Generate Both Versions
```bash
# Generate standard version
python card.py -c 10 -f batt_standard.py

# Generate vectorized version  
python card.py -c 10 -f batt_vectorized.py --vectorized
```

### Test 2: Compare Structure
```bash
# Check standard has try/except
grep -c "try:" batt_standard.py

# Check vectorized has no try/except
grep -c "try:" batt_vectorized.py  # Should be 0
```

### Test 3: Run Single Sample
```python
# Test standard
result1 = batt(task_id, S, I, C, log_path)

# Test vectorized (single item batch)
result2 = batt_vectorized([(task_id, S, I, C)])

# Compare
assert result1 == result2[0]
```

## ⏱️ Timeline

**Day 1 Morning** (4 hours):
- Task 1: Add flag (30 min)
- Task 2: Modify Code class (2 hours)
- Task 3: Start batch-friendly generation (1.5 hours)

**Day 1 Afternoon** (4 hours):
- Task 3: Complete batch generation (1.5 hours)
- Task 4: Validation helpers (2 hours)
- Buffer time (30 min)

**Day 2 Morning** (4 hours):
- Task 5: Test generation (2 hours)
- Debug and fix issues (2 hours)

**Day 2 Afternoon** (4 hours):
- Validation and correctness testing
- Documentation
- Commit and prepare for Day 3-4

## 📊 Success Criteria

- [ ] Can generate both batt() and batt_vectorized()
- [ ] Vectorized version has NO try/except blocks
- [ ] Single-sample batch produces same result as standard
- [ ] Generated code is syntactically valid
- [ ] Ready for GPU batch coordinator (Day 3-4)

---

**Status**: Ready to start!  
**Next**: Implement Task 1 (Add command-line flag)

# Week 6B: Production Monitoring Guide

**Quick reference for monitoring Week 6B parallel processing in production**

---

## Key Log Patterns to Watch

### Normal Operation ✅

```
Running: python run_batt.py -t 10.0 -c -32 -b tmp_batt_xxx
# No "System overloaded" message → ProcessPoolExecutor used
# No "failed" messages → Parallel execution successful
```

**What it means**: System healthy, using ProcessPoolExecutor (3 workers)

---

### High Load ⚠️

```
-- System overloaded (65 threads), using sequential processing
```

**What it means**: 
- Thread count > 50, ProcessPoolExecutor skipped
- Using ThreadPoolExecutor (1 worker) or sequential
- Expected in multi-instance environment
- **ACTION**: Normal, no action needed (graceful degradation)

---

### Memory Pressure ⚠️

```
-- ProcessPoolExecutor failed (OSError: [Errno 12] Cannot allocate memory), trying ThreadPoolExecutor
```

**What it means**:
- ProcessPoolExecutor couldn't allocate memory
- Falling back to ThreadPoolExecutor (1 worker)
- Expected under memory constraints
- **ACTION**: Monitor frequency, consider reducing concurrent instances if > 50%

---

### ThreadPool Fallback ⚠️

```
-- ThreadPoolExecutor also failed (...), using sequential processing
```

**What it means**:
- Both ProcessPool and ThreadPool failed
- Using sequential processing (no parallelism)
- Expected under extreme resource pressure
- **ACTION**: If frequent (> 30%), system is overloaded

---

### Script Timeout ❌

```
bash run_card.sh timeout after 600s
```

**What it means**:
- Script ran for 10 minutes without completing
- Killed by timeout mechanism
- Likely hanging on thread creation
- **ACTION**: Check thread count threshold (may need to reduce from 50)

---

## Monitoring Commands

### Check Active Thread Count
```bash
# Python script
python -c "import threading; print(f'Active threads: {threading.active_count()}')"

# System-wide (Linux)
ps -eLf | wc -l

# Per-process (Linux)
ps -o nlwp <PID>
```

### Monitor Log Patterns
```bash
# Watch for fallbacks
tail -f tmp_batt_*_run.log | grep -E "overloaded|failed|trying|fallback"

# Count fallback occurrences
grep -c "ProcessPoolExecutor failed" tmp_batt_*_run.log
grep -c "ThreadPoolExecutor also failed" tmp_batt_*_run.log
grep -c "System overloaded" tmp_batt_*_run.log
```

### Check Timeout Frequency
```bash
# Count timeouts
grep -c "timeout" run_card.sh logs

# Average script runtime
grep "Running:" tmp_batt_*_run.log | head -10
```

---

## Health Check Thresholds

| Metric | Healthy | Warning | Critical | Action |
|--------|---------|---------|----------|--------|
| Thread count | < 50 | 50-80 | > 80 | Reduce concurrent instances |
| ProcessPool fallback | < 10% | 10-30% | > 30% | Add memory or reduce workers |
| ThreadPool fallback | < 5% | 5-15% | > 15% | Reduce concurrent instances |
| Script timeouts | 0% | < 5% | > 5% | Investigate hangs |
| Active threads per instance | < 15 | 15-25 | > 25 | Resource leak? |

---

## Quick Diagnostics

### Scenario 1: Frequent "System overloaded" Messages

**Symptoms**:
```
-- System overloaded (65 threads), using sequential processing
-- System overloaded (72 threads), using sequential processing
-- System overloaded (58 threads), using sequential processing
```

**Diagnosis**: Too many concurrent run_card.sh instances

**Solutions**:
1. Reduce concurrent instances (8 → 4-6)
2. Increase threshold (50 → 70) if system stable
3. Monitor system thread count before starting new instances

---

### Scenario 2: Frequent ProcessPool Fallbacks

**Symptoms**:
```
-- ProcessPoolExecutor failed (OSError: [Errno 12] Cannot allocate memory), trying ThreadPoolExecutor
```

**Diagnosis**: Memory pressure, not enough RAM for 3 worker processes

**Solutions**:
1. Reduce concurrent instances
2. Add more system memory
3. Reduce ProcessPoolExecutor workers (3 → 2) if needed
4. This is working as designed (fallback successful)

---

### Scenario 3: Script Timeouts

**Symptoms**:
```
timeout: sending signal TERM to command 'python'
```

**Diagnosis**: Script hanging, likely on thread creation despite checks

**Solutions**:
1. Check thread count before timeout: `ps -eLf | wc -l`
2. Reduce thread threshold (50 → 30-40)
3. Increase timeout (600s → 900s) if legitimate work
4. Check for thread leaks: `lsof -p <PID> | grep -c thread`

---

### Scenario 4: Sequential Fallback Excessive

**Symptoms**:
```
-- ThreadPoolExecutor also failed (...), using sequential processing
```
(Appearing in > 30% of runs)

**Diagnosis**: System severely overloaded

**Solutions**:
1. Reduce concurrent instances significantly (8 → 2-3)
2. Check for other resource-heavy processes
3. Consider running single-instance until resource issue resolved
4. This still works (sequential is reliable), just slower

---

## Performance Expectations

### Normal Load (<50 threads)

| Samples | Executor | Workers | Expected Time | Notes |
|---------|----------|---------|---------------|-------|
| 2-3 | Thread | 3 | ~1-2s | Small batch, threads optimal |
| 6-8 | Process | 3 | ~2-4s | Large batch, 20-30% faster |
| 32+ | Process | 3 | ~10-20s | Full batch, good parallelism |

### High Load (50-80 threads)

| Samples | Executor | Workers | Expected Time | Notes |
|---------|----------|---------|---------------|-------|
| Any | Thread | 1 | 1.5-2x normal | Minimal threading |
| Any | Sequential | 1 | 2-3x normal | No parallelism |

### Extreme Load (>80 threads)

| Samples | Executor | Workers | Expected Time | Notes |
|---------|----------|---------|---------------|-------|
| Any | Sequential | 1 | 2-3x normal | Functional, degraded performance |

---

## Automated Monitoring Script

Save as `monitor_week6b.sh`:

```bash
#!/bin/bash

# Week 6B Production Monitoring
# Run in background: bash monitor_week6b.sh &

LOG_FILE="week6b_monitoring.log"
CHECK_INTERVAL=60  # Check every 60 seconds

echo "=== Week 6B Monitoring Started ===" | tee -a $LOG_FILE
date | tee -a $LOG_FILE

while true; do
    # Get current metrics
    THREADS=$(python -c "import threading; print(threading.active_count())" 2>/dev/null || echo "N/A")
    SYSTEM_THREADS=$(ps -eLf 2>/dev/null | wc -l || echo "N/A")
    
    # Count recent fallbacks (last 100 lines)
    PROCESS_FAILS=$(tail -100 tmp_batt_*_run.log 2>/dev/null | grep -c "ProcessPoolExecutor failed" || echo "0")
    THREAD_FAILS=$(tail -100 tmp_batt_*_run.log 2>/dev/null | grep -c "ThreadPoolExecutor also failed" || echo "0")
    OVERLOADED=$(tail -100 tmp_batt_*_run.log 2>/dev/null | grep -c "System overloaded" || echo "0")
    
    # Log status
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    echo "$TIMESTAMP | Threads: Python=$THREADS System=$SYSTEM_THREADS | Fails: Process=$PROCESS_FAILS Thread=$THREAD_FAILS Overload=$OVERLOADED" | tee -a $LOG_FILE
    
    # Alert on critical conditions
    if [ "$OVERLOADED" -gt 5 ]; then
        echo "⚠️  ALERT: System overloaded detected $OVERLOADED times in last 100 lines" | tee -a $LOG_FILE
    fi
    
    if [ "$THREAD_FAILS" -gt 3 ]; then
        echo "❌ ALERT: ThreadPool failures $THREAD_FAILS times (extreme load)" | tee -a $LOG_FILE
    fi
    
    sleep $CHECK_INTERVAL
done
```

**Usage**:
```bash
# Start monitoring
bash monitor_week6b.sh &

# View live
tail -f week6b_monitoring.log

# Stop monitoring
pkill -f monitor_week6b.sh
```

---

## Troubleshooting Decision Tree

```
Is script completing successfully?
├─ YES → Check logs for fallback patterns
│  ├─ No fallbacks → ✅ Optimal performance
│  ├─ ProcessPool fallbacks (<30%) → ✅ Working as designed
│  ├─ ThreadPool fallbacks (<15%) → ⚠️ Monitor, consider reducing load
│  └─ Sequential fallbacks (>30%) → ❌ System overloaded, reduce instances
│
└─ NO → Script hanging or timing out?
   ├─ Hanging → Check thread count
   │  ├─ >80 threads → ❌ Thread exhaustion despite checks
   │  │  └─ ACTION: Reduce threshold (50 → 30)
   │  └─ <50 threads → ❌ Other issue (deadlock? infinite loop?)
   │     └─ ACTION: Check code logic, add logging
   │
   └─ Timing out (10 minutes) → Legitimate work or hang?
      ├─ Legitimate (large batch) → Increase timeout (600s → 900s)
      └─ Hang → See "Hanging" above
```

---

## Expected Production Patterns

### Healthy Production (8 concurrent instances)

```
Instance 1: ProcessPoolExecutor (3 workers) ✓
Instance 2: ProcessPoolExecutor (3 workers) ✓
Instance 3: ThreadPoolExecutor (1 worker) - some pressure ✓
Instance 4: ProcessPoolExecutor (3 workers) ✓
Instance 5: Sequential - high load ✓
Instance 6: ProcessPoolExecutor (3 workers) ✓
Instance 7: ThreadPoolExecutor (1 worker) - some pressure ✓
Instance 8: ProcessPoolExecutor (3 workers) ✓

Overall: 75% ProcessPool, 15% ThreadPool, 10% Sequential
Thread count: 40-60 threads (fluctuating)
Fallback rate: 10-20% (acceptable)
```

### Overloaded Production (needs tuning)

```
Instance 1: Sequential - overloaded ❌
Instance 2: Sequential - overloaded ❌
Instance 3: ThreadPoolExecutor fails, sequential ❌
Instance 4: Sequential - overloaded ❌
Instance 5: Sequential - overloaded ❌
Instance 6: Timeout after 10 minutes ❌
Instance 7: Sequential - overloaded ❌
Instance 8: Sequential - overloaded ❌

Overall: 0% ProcessPool, 0% ThreadPool, 100% Sequential
Thread count: >80 threads (constant)
Fallback rate: 100% (system overloaded)
```

**ACTION**: Reduce instances from 8 to 4, or reduce threshold from 50 to 30

---

## Summary: What to Watch

### 🟢 Green Flags (Everything Good)
- Thread count < 50 most of the time
- ProcessPoolExecutor used in >70% of runs
- No timeouts
- Fallback rate < 20%

### 🟡 Yellow Flags (Monitor Closely)
- Thread count 50-80 occasionally
- ProcessPool fallback 20-30%
- ThreadPool fallback 10-15%
- Occasional "System overloaded" messages

### 🔴 Red Flags (Take Action)
- Thread count > 80 frequently
- ProcessPool fallback > 30%
- ThreadPool fallback > 15%
- Script timeouts
- Frequent "System overloaded" messages

---

**Quick Reference**: Keep this document open during production deployment and refer to it when investigating issues.

**Related Documents**:
- WEEK6B_PRODUCTION_DEPLOYMENT_SUMMARY.md - Complete issue history
- WEEK6B_THREAD_EXHAUSTION_FIX.md - Thread exhaustion details
- WEEK6B_PRODUCTION_FIXES.md - Memory and threading fixes

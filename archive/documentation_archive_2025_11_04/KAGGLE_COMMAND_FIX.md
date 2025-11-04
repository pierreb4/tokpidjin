# 🔧 KAGGLE COMMAND CORRECTION - QUICK FIX

**What You Tried**:
```bash
python run_batt.py -c 100 --gpu --profile
```

**Error**:
```
unrecognized arguments: --gpu --profile
```

**Why**: These arguments don't exist in run_batt.py

---

## ✅ CORRECTED COMMANDS

### Use This Instead:

**Option 1 - Full Profiling (Recommended)**:
```bash
python run_batt.py -c 100 --cprofile --cprofile-top 30
```

**Option 2 - Quick Wall-Clock**:
```bash
python run_batt.py -c 100 --timing
```

---

## Key Points

✅ **GPU auto-detects** - No need for explicit `--gpu` flag  
✅ **Use `--cprofile`** - Not `--profile` (that's not a valid argument)  
✅ **Use `--timing`** - For lightweight timing breakdown  
✅ **Both work** - Choose based on whether you want detailed profiling or quick measurement

---

## Expected Output

With `--cprofile`:
```
Kaggle GPU Support: True (1 devices)
  GPU 0: Compute 7.5, Memory: 24.0GB

... profiler output ...

objects    3400 calls    ~1.2-1.3s  (IMPROVED from 1.402s)
Wall-clock: 3.10s
```

With `--timing`:
```
Framework: 2.12s
DSL: 0.98s
Wall-clock: 3.10s
```

---

## Next Steps

1. Pull latest: `git pull origin main` (commit dde871b5)
2. Run: `python run_batt.py -c 100 --cprofile --cprofile-top 30`
3. Measure wall-clock time (expect 3.08-3.15s vs 3.23s baseline)
4. Check objects() improved from 1.402s to ~1.2-1.3s
5. Document results

---

**Status**: ✅ Ready for corrected validation!

# Mega-Batch Quick Start Guide

## Generate Vectorized Batt

```bash
# Generate with 10 tasks
python card.py -c 10 -f my_batt.py --vectorized

# Generate with all tasks
python card.py -c -1 -f my_batt.py --vectorized

# Generate specific task
python card.py -i task_id -f my_batt.py --vectorized
```

## Run Mega-Batch Mode

```bash
# Basic usage (first 10 tasks)
python run_batt.py --mega-batch -c 10 -b my_batt --timing

# Custom batch size
python run_batt.py --mega-batch -c 10 -b my_batt --batch-size 500

# Specific tasks
python run_batt.py --mega-batch -i task1 task2 task3 -b my_batt --timing

# All tasks (Week 5 with GPU)
python run_batt.py --mega-batch -b my_batt
```

## Compare with Standard Mode

```bash
# Standard mode (traditional)
python run_batt.py -c 10 -b my_batt --timing

# Mega-batch mode (new)
python run_batt.py --mega-batch -c 10 -b my_batt --timing
```

## Flags

### card.py
- `--vectorized` - Generate GPU-compatible code (no try/except)
- `-c N` - Number of tasks (use -1 for all)
- `-f FILE.py` - Output filename (must end in .py)

### run_batt.py
- `--mega-batch` - Use mega-batch processing
- `--batch-size N` - Samples per batch (default: 1000)
- `--timing` - Show performance breakdown
- `-c N` - Number of tasks to process
- `-i TASKS` - Specific task IDs
- `-b MODULE` - Batt module name (without .py)

## Expected Output

```
============================================================
MEGA-BATCH MODE - GPU Batch Processing
============================================================
Batch size: 1000
Batt module: my_batt
Processing 10 tasks

Collecting inputs from all tasks...

============================================================
MEGA-BATCH RESULTS
============================================================
Total time: X.XXXs
Tasks processed: 10
Total samples: XX
Total candidates: XXX
Average time per sample: X.XXms
Average time per task: X.XXXs

Performance Notes:
  - This is CPU sequential baseline (Week 4)
  - Week 5 will add GPU vectorization
  - Expected Week 5 speedup: 4.8-9x faster
  - Projected GPU time: X.XXXs (assuming 6x speedup)
============================================================
```

## Week 5 (Coming Soon)

When GPU integration is complete:
- Same commands work automatically
- Detects GPU availability
- 4.8-9x speedup vs CPU baseline
- Automatic fallback to CPU if no GPU

## Troubleshooting

### "Module has no batt function"
- Make sure file ends with `.py`: `my_batt.py` not `my_batt`
- Regenerate: `python card.py -c 10 -f my_batt.py --vectorized`

### "IndentationError"
- Old version of card.py had bug (fixed)
- Regenerate with latest card.py

### Slow performance
- This is expected in Week 4 (CPU baseline)
- Week 5 will add GPU acceleration (4.8-9x faster)

## Tips

1. **Start small**: Test with `-c 3` first
2. **Use --timing**: Shows performance breakdown
3. **Batch size**: 1000 is good default, tune for your GPU
4. **CPU vs GPU**: CPU baseline useful for comparison
5. **Vectorized only**: Must use vectorized batt for mega-batch mode

## Next Steps

Ready for Week 5 GPU integration! 🚀

# Week 2 Correctness Debugging

## 🐛 CRITICAL BUG IDENTIFIED

**Status:** 2 out of 3 solvers failing correctness tests

### Symptoms

| Solver | CPU Result | GPU Result | Issue |
|--------|------------|------------|-------|
| solve_23b5c85d | `((7, 7), (7, 0))` | `((4, 4), (4, 0))` | **Wrong color!** (7→4) |
| solve_1f85a75f | color 3 grid | color 1 grid | **Wrong color!** (3→1) |
| solve_09629e4f | ✓ Match | ✓ Match | Correct (but slow) |

### Analysis

**Key Observation:** Shapes are correct, only colors differ!

This suggests:
- Connected components work correctly ✓
- Object extraction positions are correct ✓  
- But **color values** or **object ordering** is wrong ✗

### Possible Root Causes

1. **Color extraction bug** in `gpu_dsl_core.py`:
   - Line 170: `color = int(grid_cpu[i, j])` - is this getting wrong values?
   - Line 237: `obj.append((i, j, color_int))` - is color_int wrong?

2. **Object ordering bug**:
   - CPU and GPU return objects in different order
   - `get_arg_rank_f` selects by position in list
   - Different order → wrong object selected → wrong color

3. **Label vs Color confusion**:
   - Connected components return label IDs (1, 2, 3...)
   - Are we using label ID instead of grid color value?

### Most Likely: Object Ordering

Looking at the solver logic:
```python
x1 = gpu_o_g(I, R7)              # Extract objects
x2 = get_arg_rank_f(x1, size, L1)  # Get largest object
O = subgrid(x2, I)                 # Extract subgrid
```

If `gpu_o_g` returns objects in different order than CPU `o_g`:
- `get_arg_rank_f` sorts by size, but ties broken by **list order**
- Different order → different object selected
- Wrong object → wrong color in result

**Evidence from debug output:**
- CPU: 7 objects, colors {1,2,3,4,5,6,7}
- Sizes: [3,3,3,6,8,10,10] - TWO size-3 objects (colors 4 and 7)
- If GPU returns them in opposite order → wrong object selected!

---

## 🔍 Debug Steps

### Step 1: Upload Debug Script to Kaggle

**Files to upload:**
- `kaggle_debug_gpu_o_g.py` (NEW debug script)
- `gpu_dsl_core.py`
- `dsl.py`
- `constants.py`
- `arc_types.py`

### Step 2: Run Debug Script

```bash
!python kaggle_debug_gpu_o_g.py
```

### Step 3: Check Output

**What to look for:**

1. **Object count match?**
   ```
   CPU: Number of objects: 7
   GPU: Number of objects: 7
   ```
   ✓ Should match (7 objects)

2. **Object sizes match?**
   ```
   CPU sizes: [3, 3, 3, 6, 8, 10, 10]
   GPU sizes: [3, 3, 3, 6, 8, 10, 10]
   ```
   ✓ Should match

3. **Object colors match?**
   ```
   Object 0: size= 3, CPU color={4}, GPU color={4}
   Object 1: size= 3, CPU color={6}, GPU color={6}
   Object 2: size= 3, CPU color={7}, GPU color={7}
   ```
   
   **This is the critical check!** If colors don't match:
   - → Color extraction bug (check lines 170, 237 in gpu_dsl_core.py)
   
   If colors match but in different order:
   - → Object ordering bug (need to match CPU ordering)

### Step 4: Report Findings

Copy the full output, especially the "Detailed comparison" section showing which objects differ.

---

## 🔧 Potential Fixes

### Fix 1: If Color Extraction Bug

Check `gpu_dsl_core.py` line 170 and 237:
```python
color = int(grid_cpu[i, j])  # Are i,j indices correct?
```

Maybe indices are swapped or offset?

### Fix 2: If Object Ordering Bug

The issue is `cupyx.scipy.ndimage.label` may return labels in different order than CPU.

**Solution:** Sort objects consistently before returning:
```python
# In gpu_o_g, before returning:
objects_list.sort(key=lambda obj: (
    min(cell[0] for cell in obj),  # Min row
    min(cell[1] for cell in obj),  # Min col
    len(obj),                       # Size
))
```

This ensures GPU and CPU return objects in same order.

### Fix 3: If Label ID Confusion

If GPU is returning label IDs (1,2,3...) instead of grid colors:
- Check that we're using `grid_cpu[i,j]` not `labels_cpu[i,j]`
- Line 170: `color = int(grid_cpu[i, j])` ✓ (looks correct)
- Line 237: `obj.append((i, j, color_int))` ✓ (looks correct)

---

## 📊 Expected Debug Output

### If Ordering Bug (Most Likely)

```
✓ Object sizes MATCH
✗ But object contents DIFFER

Detailed comparison:
  ✓ size= 3: CPU color={4}, GPU color={4}, positions_match=True
  ✓ size= 3: CPU color={6}, GPU color={6}, positions_match=True  
  ✗ size= 3: CPU color={7}, GPU color={4}, positions_match=True  # <-- MISMATCH!
  ✓ size= 6: CPU color={2}, GPU color={2}, positions_match=True
  ...
```

This would show: **Same positions, different colors** → ordering bug or color extraction bug.

### If Color Extraction Bug (Less Likely)

```
✗ Results DON'T MATCH
✗ Object sizes DIFFER
CPU sizes: [3, 3, 3, 6, 8, 10, 10]
GPU sizes: [3, 3, 3, 6, 8, 10, 10]  # Sizes match
✗ But object contents DIFFER

Detailed comparison shows positions_match=False
```

This would show: **Different positions** → connected components bug (unlikely, since Week 1 tests passed).

---

## 🎯 Next Actions

1. **Run `kaggle_debug_gpu_o_g.py` on Kaggle**
2. **Report full output here**
3. **Based on output, I'll implement the fix**
4. **Re-test with `benchmark_gpu_solvers.py`**
5. **Target:** 3/3 correctness, then optimize performance

---

**Priority:** Fix correctness first, performance second.

The good news: Week 1 tests all passed (128/128), so the GPU connected components logic is sound. This is likely a simpler ordering or iteration bug.


try:
    import cupy as cp
    x = cp.array([1, 2, 3])
    y = cp.linalg.norm(x)
    print("CuPy works! Norm:", y)
except Exception as e:
    print("CuPy failed:", e)

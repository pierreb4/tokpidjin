"""
GPU-accelerated versions of profiled solvers.

Week 2: Integrating gpu_o_g into actual solvers to measure end-to-end performance.

Target solvers (from profiling):
- solve_23b5c85d: 8.2ms CPU, o_g = 92% (7.5ms)
- solve_09629e4f: 6.8ms CPU, o_g = 82% (5.6ms)
- solve_1f85a75f: 5.4ms CPU, o_g = 75% (4.0ms)

Expected speedup: 1.7-2.1x end-to-end
"""

from gpu_dsl_core import gpu_o_g
# Import all other DSL functions (unchanged)
from dsl import (
    get_arg_rank_f, subgrid, size, get_arg_rank, numcolors_f, normalize,
    upscale_f, paint, f_ofcolor, fill, color
)
from constants import *


def gpu_solve_23b5c85d(S, I, C):
    """
    GPU-accelerated version of solve_23b5c85d.
    
    Original solver:
        x1 = o_g(I, R7)             # 7.5ms (92% of execution)
        x2 = get_arg_rank_f(x1, size, L1)
        O = subgrid(x2, I)
        return O
    
    Change: o_g → gpu_o_g
    Expected: 8.2ms → 4-5ms (1.7-2.0x speedup)
    """
    x1 = gpu_o_g(I, R7)  # GPU-accelerated!
    x2 = get_arg_rank_f(x1, size, L1)
    O = subgrid(x2, I)
    return O


def gpu_solve_09629e4f(S, I, C):
    """
    GPU-accelerated version of solve_09629e4f.
    
    Original solver:
        x1 = o_g(I, R3)             # 5.6ms (82% of execution)
        x2 = get_arg_rank(x1, numcolors_f, L1)
        x3 = normalize(x2)
        x4 = upscale_f(x3, FOUR)
        x5 = paint(I, x4)
        x6 = f_ofcolor(I, FIVE)
        O = fill(x5, FIVE, x6)
        return O
    
    Change: o_g → gpu_o_g
    Expected: 6.8ms → 3-4ms (1.8-2.3x speedup)
    """
    x1 = gpu_o_g(I, R3)  # GPU-accelerated!
    x2 = get_arg_rank(x1, numcolors_f, L1)
    x3 = normalize(x2)
    x4 = upscale_f(x3, FOUR)
    x5 = paint(I, x4)
    x6 = f_ofcolor(I, FIVE)
    O = fill(x5, FIVE, x6)
    return O


def gpu_solve_1f85a75f(S, I, C):
    """
    GPU-accelerated version of solve_1f85a75f.
    
    Original solver:
        x1 = o_g(I, R7)             # 4.0ms (75% of execution)
        x2 = get_arg_rank_f(x1, size, F0)
        O = subgrid(x2, I)
        return O
    
    Change: o_g → gpu_o_g
    Expected: 5.4ms → 2.2-3.0ms (1.6-2.0x speedup)
    """
    x1 = gpu_o_g(I, R7)  # GPU-accelerated!
    x2 = get_arg_rank_f(x1, size, F0)
    O = subgrid(x2, I)
    return O


# For easy import
GPU_SOLVERS = {
    '23b5c85d': gpu_solve_23b5c85d,
    '09629e4f': gpu_solve_09629e4f,
    '1f85a75f': gpu_solve_1f85a75f,
}


if __name__ == '__main__':
    print("GPU Solvers Ready:")
    for name, func in GPU_SOLVERS.items():
        print(f"  - {name}: {func.__name__}")

"""
GPU-optimized solvers using hybrid CPU/GPU strategy.

These solvers automatically use CPU or GPU based on grid size,
providing optimal performance across all input sizes.
"""

from gpu_hybrid import o_g_hybrid
from dsl import *
from constants import *


def gpu_solve_23b5c85d_hybrid(S, I, C):
    """
    Hybrid version of solve_23b5c85d.
    Automatically uses CPU for small grids, GPU for large grids.
    
    Original: x1 = o_g(I, R7); x2 = get_arg_rank_f(x1, size, L1); O = subgrid(x2, I)
    """
    x1 = o_g_hybrid(I, R7)  # Auto CPU/GPU selection
    x2 = get_arg_rank_f(x1, size, L1)
    O = subgrid(x2, I)
    return O


def gpu_solve_09629e4f_hybrid(S, I, C):
    """
    Hybrid version of solve_09629e4f.
    
    Original: x1 = o_g(I, R3); x2 = get_arg_rank(x1, numcolors_f, L1);
              x3 = normalize(x2); x4 = upscale_f(x3, FOUR);
              x5 = paint(I, x4); x6 = f_ofcolor(I, FIVE); O = fill(x5, FIVE, x6)
    """
    x1 = o_g_hybrid(I, R3)  # Auto CPU/GPU selection
    x2 = get_arg_rank(x1, numcolors_f, L1)
    x3 = normalize(x2)
    x4 = upscale_f(x3, FOUR)
    x5 = paint(I, x4)
    x6 = f_ofcolor(I, FIVE)
    O = fill(x5, FIVE, x6)
    return O


def gpu_solve_1f85a75f_hybrid(S, I, C):
    """
    Hybrid version of solve_1f85a75f.
    
    Original: x1 = o_g(I, R7); x2 = get_arg_rank_f(x1, size, F0); O = subgrid(x2, I)
    """
    x1 = o_g_hybrid(I, R7)  # Auto CPU/GPU selection
    x2 = get_arg_rank_f(x1, size, F0)
    O = subgrid(x2, I)
    return O


def gpu_solve_36d67576_hybrid(S, I, C):
    """
    Hybrid version of solve_36d67576 (120ms solver).
    """
    x1 = lbind(lbind, shift)
    x2 = compose(x1, normalize)
    x3 = lbind(rbind, subtract)
    x4 = rbind(corner, R0)
    x5 = compose(x3, x4)
    x6 = astuple(TWO, FOUR)
    x7 = rbind(contained, x6)
    x8 = rbind(get_nth_f, F0)
    x9 = compose(x7, x8)
    x10 = rbind(sfilter, x9)
    x11 = chain(x5, x10, normalize)
    x12 = lbind(occurrences, I)
    x13 = chain(x12, x10, normalize)
    x14 = fork(apply, x11, x13)
    x15 = fork(mapply, x2, x14)
    x16 = rbind(mir_rot_f, R3)
    x17 = rbind(mir_rot_f, R1)
    x18 = astuple(x16, x17)
    x19 = rbind(mir_rot_f, R0)
    x20 = rbind(mir_rot_f, R2)
    x21 = astuple(x19, x20)
    x22 = combine(x18, x21)
    x23 = rbind(get_nth_f, L1)
    x24 = fork(compose, x8, x23)
    x25 = product(x22, x22)
    x26 = apply(x24, x25)
    x27 = totuple(x26)
    x28 = combine(x22, x27)
    x29 = o_g_hybrid(I, R1)  # Auto CPU/GPU selection
    x30 = get_arg_rank_f(x29, numcolors_f, F0)
    x31 = rapply_t(x28, x30)
    x32 = mapply(x15, x31)
    O = paint(I, x32)
    return O


def gpu_solve_36fdfd69_hybrid(S, I, C):
    """
    Hybrid version of solve_36fdfd69 (58ms solver).
    """
    x1 = upscale_t(I, TWO)
    x2 = o_g_hybrid(x1, R7)  # Auto CPU/GPU selection
    x3 = colorfilter(x2, TWO)
    x4 = product(x3, x3)
    x5 = lbind(greater, FIVE)
    x6 = rbind(get_nth_f, F0)
    x7 = rbind(get_nth_f, L1)
    x8 = fork(manhattan, x6, x7)
    x9 = compose(x5, x8)
    x10 = sfilter_f(x4, x9)
    x11 = apply(merge, x10)
    x12 = mapply(delta, x11)
    x13 = fill(x1, FOUR, x12)
    x14 = merge(x3)
    x15 = paint(x13, x14)
    O = downscale(x15, TWO)
    return O


def gpu_solve_1a07d186_hybrid(S, I, C):
    """
    Hybrid version of solve_1a07d186 (11ms solver).
    """
    x1 = o_g_hybrid(I, R5)  # Auto CPU/GPU selection
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = rbind(get_nth_f, F0)
    x6 = difference(x1, x2)
    x7 = lbind(colorfilter, x6)
    x8 = chain(x5, x7, color)
    x9 = fork(gravitate, identity, x8)
    x10 = fork(shift, identity, x9)
    x11 = apply(color, x6)
    x12 = rbind(contained, x11)
    x13 = compose(x12, color)
    x14 = sfilter_f(x2, x13)
    x15 = mapply(x10, x14)
    O = paint(x4, x15)
    return O


# Convenience dictionary for easy access
HYBRID_SOLVERS = {
    '23b5c85d': gpu_solve_23b5c85d_hybrid,
    '09629e4f': gpu_solve_09629e4f_hybrid,
    '1f85a75f': gpu_solve_1f85a75f_hybrid,
    '36d67576': gpu_solve_36d67576_hybrid,
    '36fdfd69': gpu_solve_36fdfd69_hybrid,
    '1a07d186': gpu_solve_1a07d186_hybrid,
}


if __name__ == '__main__':
    print("GPU Hybrid Solvers")
    print("=" * 70)
    print(f"Available solvers: {len(HYBRID_SOLVERS)}")
    for solver_id in HYBRID_SOLVERS:
        print(f"  - {solver_id}")
    print()
    print("These solvers automatically use CPU or GPU based on grid size.")
    print("Expected performance:")
    print("  - Small grids (<8×8): Matches CPU speed")
    print("  - Large grids (≥10×10): 1.5-2x faster than CPU")
    print("  - Mixed workload: 30-50% better than pure GPU or pure CPU")

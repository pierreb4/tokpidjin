def get_3906de3d_x4_x3(a1: Callable, a2: Tuple[Tuple[int]]) -> Tuple[Tuple[int]]:
    return apply(a1, switch(a2, ONE, TWO))

# {'a1': 'Callable', 'return': 'Tuple[Tuple[int]]', 'a2': 'Tuple[Tuple[int]]'}

func_d = {('get_3906de3d_x4_x3', 'Tuple[Tuple[int]]', 'Callable', 'Tuple[Tuple[int]]'): 'apply(a1, switch(a2, ONE, TWO))'}


def get_f15e1fac_x30_x29(a1: Callable, a2: Callable) -> Callable:
    return lbind(compose, fork(both, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_f15e1fac_x30_x29', 'Callable', 'Callable', 'Callable'): 'lbind(compose, fork(both, a1, a2))'}


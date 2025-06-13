def get_72322fa7_x19_x8(a1: Callable) -> Callable:
    return fork(difference, identity, fork(sfilter, identity, a1))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_72322fa7_x19_x8', 'Callable', 'Callable'): 'fork(difference, identity, fork(sfilter, identity, a1))'}


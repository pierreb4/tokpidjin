def get_b775ac94_x19_x8(a1: Callable) -> Callable:
    return lbind(compose, fork(sfilter, identity, a1))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_b775ac94_x19_x8', 'Callable', 'Callable'): 'lbind(compose, fork(sfilter, identity, a1))'}


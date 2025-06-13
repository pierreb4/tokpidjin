def get_6aa20dc0_x8_x7(a1: Callable) -> Callable:
    return fork(difference, identity, fork(sfilter, identity, a1))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_6aa20dc0_x8_x7', 'Callable', 'Callable'): 'fork(difference, identity, fork(sfilter, identity, a1))'}


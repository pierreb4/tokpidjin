def get_662c240a_x4_x3(a1: Callable) -> Callable:
    return compose(flip, fork(equality, a1, identity))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_662c240a_x4_x3', 'Callable', 'Callable'): 'compose(flip, fork(equality, a1, identity))'}


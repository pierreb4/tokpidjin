def get_a8c38be5_x24_x23(a1: Callable) -> Callable:
    return fork(shift, identity, compose(a1, toindices))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_a8c38be5_x24_x23', 'Callable', 'Callable'): 'fork(shift, identity, compose(a1, toindices))'}


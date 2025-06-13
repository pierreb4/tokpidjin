def get_a8c38be5_x23_x22(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(chain(a1, a2, a3), toindices)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_a8c38be5_x23_x22', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(chain(a1, a2, a3), toindices)'}


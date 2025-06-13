def get_a64e4611_x46_x45(a1: Callable, a2: Callable) -> Callable:
    return compose(chain(a1, palette_f, a2), dneighbors)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_a64e4611_x46_x45', 'Callable', 'Callable', 'Callable'): 'compose(chain(a1, palette_f, a2), dneighbors)'}


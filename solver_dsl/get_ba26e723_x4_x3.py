def get_ba26e723_x4_x3(a1: Callable) -> Callable:
    return compose(a1, rbind(divide, THREE))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_ba26e723_x4_x3', 'Callable', 'Callable'): 'compose(a1, rbind(divide, THREE))'}


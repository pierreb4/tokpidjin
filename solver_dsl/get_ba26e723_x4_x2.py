def get_ba26e723_x4_x2(a1: Callable) -> Callable:
    return compose(rbind(multiply, THREE), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_ba26e723_x4_x2', 'Callable', 'Callable'): 'compose(rbind(multiply, THREE), a1)'}


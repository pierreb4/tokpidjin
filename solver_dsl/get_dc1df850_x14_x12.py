def get_dc1df850_x14_x12(a1: Callable) -> Callable:
    return compose(rbind(greater, ONE), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_dc1df850_x14_x12', 'Callable', 'Callable'): 'compose(rbind(greater, ONE), a1)'}


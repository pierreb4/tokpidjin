def get_ecdecbb3_x15_x12(a1: Callable, a2: Container, a3: Callable) -> Container:
    return mfilter_f(apply(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Container', 'a1': 'Callable', 'a2': 'Container'}

func_d = {('get_ecdecbb3_x15_x12', 'Container', 'Callable', 'Container', 'Callable'): 'mfilter_f(apply(a1, a2), a3)'}


def get_cbded52d_x16_x8(a1: Callable, a2: Callable, a3: Container[Container]) -> Callable:
    return mapply(fork(recolor_i, a1, a2), a3)

# {'a3': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_cbded52d_x16_x8', 'Callable', 'Callable', 'Callable', 'Container[Container]'): 'mapply(fork(recolor_i, a1, a2), a3)'}


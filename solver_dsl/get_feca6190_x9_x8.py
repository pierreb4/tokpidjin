def get_feca6190_x9_x8(a1: Callable, a2: Container[Container]) -> Callable:
    return mapply(fork(recolor_i, color, a1), a2)

# {'a2': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_feca6190_x9_x8', 'Callable', 'Callable', 'Container[Container]'): 'mapply(fork(recolor_i, color, a1), a2)'}


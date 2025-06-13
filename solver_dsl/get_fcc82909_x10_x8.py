def get_fcc82909_x10_x8(a1: Callable, a2: Container[Container]) -> Callable:
    return mapply(compose(box, a1), a2)

# {'a2': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_fcc82909_x10_x8', 'Callable', 'Callable', 'Container[Container]'): 'mapply(compose(box, a1), a2)'}


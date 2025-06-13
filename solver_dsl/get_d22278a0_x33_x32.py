def get_d22278a0_x33_x32(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, a2, rbind(remove, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_d22278a0_x33_x32', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, rbind(remove, a3))'}


def get_746b3537_x3_x2(a1: Callable, a2: Any) -> Callable:
    return chain(size, dedupe, a1)(a2)

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_746b3537_x3_x2', 'Callable', 'Callable', 'Any'): 'chain(size, dedupe, a1)(a2)'}


def get_eb5a1d5d_x8_x7(a1: Callable, a2: Any) -> Callable:
    return compose(a1, dedupe)(a2)

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_eb5a1d5d_x8_x7', 'Callable', 'Callable', 'Any'): 'compose(a1, dedupe)(a2)'}


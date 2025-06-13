def get_f8c80d96_x10_x7(a1: Callable, a2: Any) -> Callable:
    return chain(outbox, outbox, a1)(a2)

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_f8c80d96_x10_x7', 'Callable', 'Callable', 'Any'): 'chain(outbox, outbox, a1)(a2)'}


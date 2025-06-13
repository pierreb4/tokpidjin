def get_780d0b14_x14_x13(a1: Callable) -> Callable:
    return chain(a1, size, compose(dedupe, totuple))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_780d0b14_x14_x13', 'Callable', 'Callable'): 'chain(a1, size, compose(dedupe, totuple))'}


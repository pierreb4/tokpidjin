def get_f35d900a_x16_x15(a1: Callable) -> Callable:
    return chain(a1, lbind(rbind, manhattan), initset)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_f35d900a_x16_x15', 'Callable', 'Callable'): 'chain(a1, lbind(rbind, manhattan), initset)'}


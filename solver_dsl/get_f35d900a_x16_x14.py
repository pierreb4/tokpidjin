def get_f35d900a_x16_x14(a1: Callable) -> Callable:
    return chain(rbind(compose, initset), a1, initset)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_f35d900a_x16_x14', 'Callable', 'Callable'): 'chain(rbind(compose, initset), a1, initset)'}


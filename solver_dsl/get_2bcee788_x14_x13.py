def get_2bcee788_x14_x13(a1: Callable) -> Callable:
    return compose(flip, matcher(a1, THREE))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_2bcee788_x14_x13', 'Callable', 'Callable'): 'compose(flip, matcher(a1, THREE))'}


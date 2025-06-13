def get_d89b689b_x10_x9(a1: Callable) -> Callable:
    return compose(a1, lbind(rbind, manhattan))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_d89b689b_x10_x9', 'Callable', 'Callable'): 'compose(a1, lbind(rbind, manhattan))'}


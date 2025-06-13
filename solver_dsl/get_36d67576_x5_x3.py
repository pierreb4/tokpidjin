def get_36d67576_x5_x3(a1: Callable) -> Callable:
    return compose(lbind(rbind, subtract), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_36d67576_x5_x3', 'Callable', 'Callable'): 'compose(lbind(rbind, subtract), a1)'}


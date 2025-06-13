def get_36d67576_x10_x9(a1: Callable, a2: Callable) -> Callable:
    return rbind(sfilter, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_36d67576_x10_x9', 'Callable', 'Callable', 'Callable'): 'rbind(sfilter, compose(a1, a2))'}


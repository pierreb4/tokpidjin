def get_36d67576_x11_x10(a1: Callable, a2: Any) -> Callable:
    return chain(a1, rbind(sfilter, a2), normalize)

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_36d67576_x11_x10', 'Callable', 'Callable', 'Any'): 'chain(a1, rbind(sfilter, a2), normalize)'}


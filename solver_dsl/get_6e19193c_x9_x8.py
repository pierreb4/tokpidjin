def get_6e19193c_x9_x8(a1: Callable, a2: Any) -> Callable:
    return chain(a1, rbind(sfilter, a2), toindices)

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_6e19193c_x9_x8', 'Callable', 'Callable', 'Any'): 'chain(a1, rbind(sfilter, a2), toindices)'}


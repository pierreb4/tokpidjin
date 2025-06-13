def get_6d58a25d_x10_x8(a1: Any, a2: Callable) -> Callable:
    return compose(rbind(greater, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Any'}

func_d = {('get_6d58a25d_x10_x8', 'Callable', 'Any', 'Callable'): 'compose(rbind(greater, a1), a2)'}


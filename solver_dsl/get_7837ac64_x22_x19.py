def get_7837ac64_x22_x19(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, rbind(sfilter, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_7837ac64_x22_x19', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, rbind(sfilter, a2), a3)'}


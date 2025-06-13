def get_f15e1fac_x16_x4(a1: bool, a2: Any, a3: Callable, a4: Callable) -> Any:
    return chain(branch(a1, identity, a2), a3, a4)

# {'a3': 'Callable', 'a4': 'Callable', 'return': 'Any', 'a1': 'bool', 'a2': 'Any'}

func_d = {('get_f15e1fac_x16_x4', 'Any', 'bool', 'Any', 'Callable', 'Callable'): 'chain(branch(a1, identity, a2), a3, a4)'}


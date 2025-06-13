def get_f15e1fac_x16_x8(a1: Callable, a2: bool, a3: Any, a4: Callable) -> Any:
    return chain(a1, branch(a2, identity, a3), a4)

# {'a1': 'Callable', 'a4': 'Callable', 'return': 'Any', 'a2': 'bool', 'a3': 'Any'}

func_d = {('get_f15e1fac_x16_x8', 'Any', 'Callable', 'bool', 'Any', 'Callable'): 'chain(a1, branch(a2, identity, a3), a4)'}


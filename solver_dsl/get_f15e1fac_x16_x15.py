def get_f15e1fac_x16_x15(a1: Callable, a2: Callable, a3: bool, a4: Any) -> Any:
    return chain(a1, a2, branch(a3, identity, a4))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Any', 'a3': 'bool', 'a4': 'Any'}

func_d = {('get_f15e1fac_x16_x15', 'Any', 'Callable', 'Callable', 'bool', 'Any'): 'chain(a1, a2, branch(a3, identity, a4))'}


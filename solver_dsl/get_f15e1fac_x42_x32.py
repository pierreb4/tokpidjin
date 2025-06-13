def get_f15e1fac_x42_x32(a1: Callable, a2: Callable, a3: Callable, a4: Container) -> Callable:
    return apply(chain(a1, a2, a3), a4)

# {'a4': 'Container', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_f15e1fac_x42_x32', 'Callable', 'Callable', 'Callable', 'Callable', 'Container'): 'apply(chain(a1, a2, a3), a4)'}


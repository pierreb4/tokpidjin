def get_aba27056_x17_x16(a1: Callable, a2: Callable) -> Callable:
    return fork(shoot, a1, fork(subtract, a2, a1))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_aba27056_x17_x16', 'Callable', 'Callable', 'Callable'): 'fork(shoot, a1, fork(subtract, a2, a1))'}


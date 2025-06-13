def get_aba27056_x16_x14(a1: Callable) -> Callable:
    return fork(subtract, a1, rbind(get_nth_f, F0))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_aba27056_x16_x14', 'Callable', 'Callable'): 'fork(subtract, a1, rbind(get_nth_f, F0))'}


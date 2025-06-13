def get_aba27056_x16_x15(a1: Callable) -> Callable:
    return fork(subtract, rbind(get_nth_f, L1), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_aba27056_x16_x15', 'Callable', 'Callable'): 'fork(subtract, rbind(get_nth_f, L1), a1)'}


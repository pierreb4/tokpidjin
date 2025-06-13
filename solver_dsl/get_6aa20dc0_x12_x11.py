def get_6aa20dc0_x12_x11(a1: Callable) -> Callable:
    return fork(compose, a1, rbind(get_nth_f, L1))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_6aa20dc0_x12_x11', 'Callable', 'Callable'): 'fork(compose, a1, rbind(get_nth_f, L1))'}


def get_93b581b8_x3_x2(a1: Callable) -> Callable:
    return chain(a1, rbind(mir_rot_f, R1), merge)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_93b581b8_x3_x2', 'Callable', 'Callable'): 'chain(a1, rbind(mir_rot_f, R1), merge)'}


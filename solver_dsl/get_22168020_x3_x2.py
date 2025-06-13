def get_22168020_x3_x2(a1: Callable, a2: Any) -> Callable:
    return fork(a1, lbind(f_ofcolor, a2), lbind(f_ofcolor, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_22168020_x3_x2', 'Callable', 'Callable', 'Any'): 'fork(a1, lbind(f_ofcolor, a2), lbind(f_ofcolor, a2))'}


def get_2bee17df_x7_x6(a1: Callable, a2: Any) -> Callable:
    return lbind(apply, matcher(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_2bee17df_x7_x6', 'Callable', 'Callable', 'Any'): 'lbind(apply, matcher(a1, a2))'}


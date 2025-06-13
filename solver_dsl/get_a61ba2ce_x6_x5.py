def get_a61ba2ce_x6_x5(a1: Callable) -> Callable:
    return lbind(compose, matcher(a1, ZERO))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_a61ba2ce_x6_x5', 'Callable', 'Callable'): 'lbind(compose, matcher(a1, ZERO))'}


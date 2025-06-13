def get_b775ac94_x7_x6(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, a2, rbind(get_color_rank_f, F0))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_b775ac94_x7_x6', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, rbind(get_color_rank_f, F0))'}


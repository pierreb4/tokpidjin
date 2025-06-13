def get_f35d900a_x5_x4(a1: Callable) -> Callable:
    return fork(recolor_i, compose(a1, color), outbox)

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_f35d900a_x5_x4', 'Callable', 'Callable'): 'fork(recolor_i, compose(a1, color), outbox)'}


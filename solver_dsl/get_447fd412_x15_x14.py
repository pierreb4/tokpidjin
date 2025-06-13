def get_447fd412_x15_x14(a1: Callable) -> Callable:
    return fork(combine, identity, compose(a1, outbox))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_447fd412_x15_x14', 'Callable', 'Callable'): 'fork(combine, identity, compose(a1, outbox))'}


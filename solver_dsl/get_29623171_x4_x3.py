def get_29623171_x4_x3(a1: Callable) -> Callable:
    return fork(a1, identity, rbind(add, THREE))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_29623171_x4_x3', 'Callable', 'Callable'): 'fork(a1, identity, rbind(add, THREE))'}


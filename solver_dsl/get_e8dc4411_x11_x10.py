def get_e8dc4411_x11_x10() -> Callable:
    return fork(add, identity, fork(subtract, identity, crement))

# {'return': 'Callable'}

func_d = {('get_e8dc4411_x11_x10', 'Callable'): 'fork(add, identity, fork(subtract, identity, crement))'}


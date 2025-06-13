def get_8d510a79_x7_x1(a1: Callable) -> Callable:
    return compose(chain(toivec, decrement, double), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_8d510a79_x7_x1', 'Callable', 'Callable'): 'compose(chain(toivec, decrement, double), a1)'}


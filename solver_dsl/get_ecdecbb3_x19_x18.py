def get_ecdecbb3_x19_x18(a1: FrozenSet, a2: FrozenSet) -> FrozenSet:
    return mapply(neighbors, intersection(a1, a2))

# {'return': 'FrozenSet', 'a1': 'FrozenSet', 'a2': 'FrozenSet'}

func_d = {('get_ecdecbb3_x19_x18', 'FrozenSet', 'FrozenSet', 'FrozenSet'): 'mapply(neighbors, intersection(a1, a2))'}


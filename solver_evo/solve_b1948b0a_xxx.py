def solve_b1948b0a_one(S, I):
    return switch(switch(switch(switch(I, THREE, FOUR), EIGHT, NINE), TWO, SIX), ONE, FIVE)


def solve_b1948b0a(S, I, x=0):
    x1 = switch(I, THREE, FOUR)
    if x == 1:
        return x1
    x2 = switch(x1, EIGHT, NINE)
    if x == 2:
        return x2
    x3 = switch(x2, TWO, SIX)
    if x == 3:
        return x3
    O = switch(x3, ONE, FIVE)
    return O

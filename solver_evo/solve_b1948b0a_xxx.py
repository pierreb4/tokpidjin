def solve_b1948b0a_one(S, I):
    return switch(switch(switch(switch(I, THREE, FOUR), EIGHT, NINE), TWO, SIX), ONE, FIVE)


def solve_b1948b0a(S, I):
    x1 = switch(I, THREE, FOUR)
    x2 = switch(x1, EIGHT, NINE)
    x3 = switch(x2, TWO, SIX)
    O = switch(x3, ONE, FIVE)
    return O

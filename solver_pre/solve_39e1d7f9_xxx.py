def solve_39e1d7f9_one(S, I):
    return paint(I, mapply(lbind(shift, asobject(crop(I, decrement(subtract(corner(get_arg_rank_f(colorfilter(o_g(I, R5), color(get_nth_t(remove_f(get_nth_t(order(fgpartition(I), height_f), L1), order(fgpartition(I), height_f)), L1))), chain(chain(size, lbind(remove, get_color_rank_t(I, F0)), palette_t), rbind(toobject, I), power(outbox, TWO)), F0), R0), shape_f(get_arg_rank_f(colorfilter(o_g(I, R5), color(get_nth_t(remove_f(get_nth_t(order(fgpartition(I), height_f), L1), order(fgpartition(I), height_f)), L1))), chain(chain(size, lbind(remove, get_color_rank_t(I, F0)), palette_t), rbind(toobject, I), power(outbox, TWO)), F0)))), add(multiply(shape_f(get_arg_rank_f(colorfilter(o_g(I, R5), color(get_nth_t(remove_f(get_nth_t(order(fgpartition(I), height_f), L1), order(fgpartition(I), height_f)), L1))), chain(chain(size, lbind(remove, get_color_rank_t(I, F0)), palette_t), rbind(toobject, I), power(outbox, TWO)), F0)), THREE), TWO_BY_TWO)))), apply(rbind(subtract, increment(shape_f(get_arg_rank_f(colorfilter(o_g(I, R5), color(get_nth_t(remove_f(get_nth_t(order(fgpartition(I), height_f), L1), order(fgpartition(I), height_f)), L1))), chain(chain(size, lbind(remove, get_color_rank_t(I, F0)), palette_t), rbind(toobject, I), power(outbox, TWO)), F0)))), apply(rbind(corner, R0), colorfilter(o_g(I, R5), color(get_nth_t(remove_f(get_nth_t(order(fgpartition(I), height_f), L1), order(fgpartition(I), height_f)), L1)))))))


def solve_39e1d7f9(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = order(x2, height_f)
    if x == 3:
        return x3
    x4 = get_nth_t(x3, L1)
    if x == 4:
        return x4
    x5 = remove_f(x4, x3)
    if x == 5:
        return x5
    x6 = get_nth_t(x5, L1)
    if x == 6:
        return x6
    x7 = color(x6)
    if x == 7:
        return x7
    x8 = colorfilter(x1, x7)
    if x == 8:
        return x8
    x9 = get_color_rank_t(I, F0)
    if x == 9:
        return x9
    x10 = lbind(remove, x9)
    if x == 10:
        return x10
    x11 = chain(size, x10, palette_t)
    if x == 11:
        return x11
    x12 = rbind(toobject, I)
    if x == 12:
        return x12
    x13 = power(outbox, TWO)
    if x == 13:
        return x13
    x14 = chain(x11, x12, x13)
    if x == 14:
        return x14
    x15 = get_arg_rank_f(x8, x14, F0)
    if x == 15:
        return x15
    x16 = corner(x15, R0)
    if x == 16:
        return x16
    x17 = shape_f(x15)
    if x == 17:
        return x17
    x18 = subtract(x16, x17)
    if x == 18:
        return x18
    x19 = decrement(x18)
    if x == 19:
        return x19
    x20 = multiply(x17, THREE)
    if x == 20:
        return x20
    x21 = add(x20, TWO_BY_TWO)
    if x == 21:
        return x21
    x22 = crop(I, x19, x21)
    if x == 22:
        return x22
    x23 = asobject(x22)
    if x == 23:
        return x23
    x24 = lbind(shift, x23)
    if x == 24:
        return x24
    x25 = increment(x17)
    if x == 25:
        return x25
    x26 = rbind(subtract, x25)
    if x == 26:
        return x26
    x27 = rbind(corner, R0)
    if x == 27:
        return x27
    x28 = apply(x27, x8)
    if x == 28:
        return x28
    x29 = apply(x26, x28)
    if x == 29:
        return x29
    x30 = mapply(x24, x29)
    if x == 30:
        return x30
    O = paint(I, x30)
    return O

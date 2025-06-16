from constants import *
from dsl import *


def batt(S, I, O):
    try:
        t1 = identity(p_g)
    except:
        t1 = None
    try:
        t2 = get_color_rank_t(I, L1)
    except:
        t2 = None
    try:
        t3 = mir_rot_t(I, R2)
    except:
        t3 = None
    try:
        t4 = fork(combine, vfrontier, hfrontier)
    except:
        t4 = None
    try:
        t5 = bottomhalf(I)
    except:
        t5 = None
    try:
        t6 = f_ofcolor(I, RED)
    except:
        t6 = None
    try:
        t7 = o_g(I, R5)
    except:
        t7 = None
    try:
        t8 = o_g(I, R4)
    except:
        t8 = None
    try:
        t9 = o_g(I, R7)
    except:
        t9 = None
    try:
        t10 = rbind(get_nth_f, F0)
    except:
        t10 = None
    try:
        t11 = tophalf(I)
    except:
        t11 = None
    try:
        t12 = o_g(I, R3)
    except:
        t12 = None
    try:
        t13 = numcolors_t(I)
    except:
        t13 = None
    try:
        t14 = rbind(shoot, DOWN)
    except:
        t14 = None
    try:
        t15 = rbind(mir_rot_f, R3)
    except:
        t15 = None
    try:
        t16 = hconcat(I, I)
    except:
        t16 = None
    try:
        t17 = o_g(I, R1)
    except:
        t17 = None
    try:
        t18 = rbind(mir_rot_t, R1)
    except:
        t18 = None
    try:
        t19 = shape_t(I)
    except:
        t19 = None
    try:
        t20 = fgpartition(I)
    except:
        t20 = None
    try:
        t21 = lbind(lbind, shift)
    except:
        t21 = None
    try:
        t22 = mir_rot_t(I, R6)
    except:
        t22 = None
    if t22 == O:
        return True, f'ed36ccf7 - t22'
    try:
        t23 = rbind(get_nth_f, L1)
    except:
        t23 = None
    try:
        t24 = replace(I, GRAY, BLACK)
    except:
        t24 = None
    try:
        t25 = mir_rot_t(I, R1)
    except:
        t25 = None
    if t25 == O:
        return True, f'74dd1130 - t25'
    try:
        t26 = asindices(I)
    except:
        t26 = None
    try:
        t27 = mir_rot_t(I, R5)
    except:
        t27 = None
    if t27 == O:
        return True, f'6150a2bd - t27'
    try:
        t28 = astuple(TWO, ONE)
    except:
        t28 = None
    try:
        t29 = f_ofcolor(I, BLUE)
    except:
        t29 = None
    try:
        t30 = rbind(hsplit, RED)
    except:
        t30 = None
    try:
        t31 = palette_t(I)
    except:
        t31 = None
    try:
        t32 = a_mr(S)
    except:
        t32 = None
    try:
        t33 = hsplit(I, THREE)
    except:
        t33 = None
    try:
        t34 = compose(neighbors, center)
    except:
        t34 = None
    try:
        t35 = crop(I, ORIGIN, THREE_BY_THREE)
    except:
        t35 = None
    try:
        t36 = rbind(get_arg_rank, F0)
    except:
        t36 = None
    try:
        t37 = interval(ONE, NINE, ONE)
    except:
        t37 = None
    try:
        t38 = index(I, ORIGIN)
    except:
        t38 = None
    try:
        t39 = astuple(NINE, NINE)
    except:
        t39 = None
    try:
        t40 = astuple(SIX, SIX)
    except:
        t40 = None
    try:
        t41 = compose(hfrontier, center)
    except:
        t41 = None
    try:
        t42 = f_ofcolor(I, THREE)
    except:
        t42 = None
    try:
        t43 = mir_rot_t(I, R0)
    except:
        t43 = None
    try:
        t44 = rbind(shoot, RIGHT)
    except:
        t44 = None
    try:
        t45 = chain(toivec, decrement, double)
    except:
        t45 = None
    try:
        t46 = rbind(order, identity)
    except:
        t46 = None
    try:
        t47 = height_t(I)
    except:
        t47 = None
    try:
        t48 = lefthalf(I)
    except:
        t48 = None
    try:
        t49 = mir_rot_t(I, R4)
    except:
        t49 = None
    try:
        t50 = get_color_rank_t(I, F0)
    except:
        t50 = None
    try:
        t51 = portrait_t(I)
    except:
        t51 = None
    try:
        t52 = upscale_t(I, TWO)
    except:
        t52 = None
    if t52 == O:
        return True, f'60c09cac - t52'
    try:
        t53 = f_ofcolor(I, GREEN)
    except:
        t53 = None
    try:
        t54 = f_ofcolor(I, GRAY)
    except:
        t54 = None
    try:
        t55 = rbind(subgrid, I)
    except:
        t55 = None
    try:
        t56 = vsplit(I, THREE)
    except:
        t56 = None
    try:
        t57 = astuple(ONE, NINE)
    except:
        t57 = None
    try:
        t58 = rbind(canvas, UNITY)
    except:
        t58 = None
    try:
        t59 = canvas(GRAY, TWO_BY_TWO)
    except:
        t59 = None
    try:
        t60 = fork(recolor_i, color, backdrop)
    except:
        t60 = None
    try:
        t61 = rbind(compose, center)
    except:
        t61 = None
    try:
        t62 = asobject(I)
    except:
        t62 = None
    try:
        t63 = fork(difference, toindices, box)
    except:
        t63 = None
    if t27 == O:
        return True, f'3c9b0459 - t27'
    try:
        t64 = astuple(ZERO, ORIGIN)
    except:
        t64 = None
    try:
        t65 = rbind(get_rank, F0)
    except:
        t65 = None
    try:
        t66 = partition(I)
    except:
        t66 = None
    try:
        t67 = lbind(index, I)
    except:
        t67 = None
    try:
        t68 = colorcount_t(I, ZERO)
    except:
        t68 = None
    try:
        t69 = crop(I, ORIGIN, TWO_BY_TWO)
    except:
        t69 = None
    if t69 == O:
        return True, f'd10ecb37 - t69'
    try:
        t70 = replace(I, RED, BLACK)
    except:
        t70 = None
    try:
        t71 = canvas(BLACK, THREE_BY_THREE)
    except:
        t71 = None
    try:
        t72 = rbind(mir_rot_t, R0)
    except:
        t72 = None
    try:
        t73 = f_ofcolor(I, CYAN)
    except:
        t73 = None
    try:
        t74 = width_t(I)
    except:
        t74 = None
    try:
        t75 = canvas(GREEN, UNITY)
    except:
        t75 = None
    if t3 == O:
        return True, f'67a3c6ac - t3'
    try:
        t76 = frontiers(I)
    except:
        t76 = None
    try:
        t77 = switch(I, THREE, FOUR)
    except:
        t77 = None
    try:
        t78 = hupscale(I, THREE)
    except:
        t78 = None
    try:
        t79 = f_ofcolor(I, YELLOW)
    except:
        t79 = None
    if t52 == O:
        return True, f'c59eb873 - t52'
    try:
        t80 = shoot(ORIGIN, UNITY)
    except:
        t80 = None
    if t25 == O:
        return True, f'9dfd6313 - t25'
    try:
        t81 = switch(I, FIVE, EIGHT)
    except:
        t81 = None
    if t81 == O:
        return True, f'd511f180 - t81'
    try:
        t82 = replace(I, GREEN, BLACK)
    except:
        t82 = None
    try:
        t83 = tojvec(SIX)
    except:
        t83 = None
    try:
        t84 = identity(S)
    except:
        t84 = None
    try:
        t85 = rbind(get_color_rank_f, L1)
    except:
        t85 = None
    try:
        t86 = upscale_t(I, THREE)
    except:
        t86 = None
    if t86 == O:
        return True, f'9172f3a0 - t86'
    try:
        t87 = astuple(TEN, TEN)
    except:
        t87 = None
    try:
        t88 = lbind(prapply, connect)
    except:
        t88 = None
    try:
        t89 = rbind(get_nth_t, F0)
    except:
        t89 = None
    try:
        t90 = rbind(get_nth_t, F1)
    except:
        t90 = None
    try:
        t91 = f_ofcolor(I, t2)
    except:
        t91 = None
    try:
        t92 = equality(t3, I)
    except:
        t92 = None
    try:
        t93 = compose(t4, center)
    except:
        t93 = None
    try:
        t94 = shape_t(t5)
    except:
        t94 = None
    try:
        t95 = center(t6)
    except:
        t95 = None
    try:
        t96 = get_nth_f(t7, F0)
    except:
        t96 = None
    try:
        t97 = hconcat(I, t3)
    except:
        t97 = None
    try:
        t98 = get_arg_rank_f(t8, size, F0)
    except:
        t98 = None
    try:
        t99 = get_nth_f(t9, F0)
    except:
        t99 = None
    try:
        t100 = compose(center, t10)
    except:
        t100 = None
    try:
        t101 = shape_t(t11)
    except:
        t101 = None
    try:
        t102 = get_nth_f(t12, F0)
    except:
        t102 = None
    try:
        t103 = decrement(t13)
    except:
        t103 = None
    try:
        t104 = compose(t14, center)
    except:
        t104 = None
    try:
        t105 = rbind(mir_rot_f, R1)
    except:
        t105 = None
    try:
        t106 = merge_f(t7)
    except:
        t106 = None
    try:
        t107 = hconcat(t16, I)
    except:
        t107 = None
    try:
        t108 = get_arg_rank_f(t17, size, L1)
    except:
        t108 = None
    try:
        t109 = righthalf(t5)
    except:
        t109 = None
    try:
        t110 = corner(t6, R3)
    except:
        t110 = None
    try:
        t111 = add(t19, TWO)
    except:
        t111 = None
    try:
        t112 = merge_f(t20)
    except:
        t112 = None
    try:
        t113 = compose(t21, normalize)
    except:
        t113 = None
    try:
        t114 = get_nth_f(t17, F0)
    except:
        t114 = None
    try:
        t115 = sizefilter(t7, EIGHT)
    except:
        t115 = None
    try:
        t116 = get_arg_rank_f(t8, height_f, F0)
    except:
        t116 = None
    try:
        t117 = lbind(sfilter, t26)
    except:
        t117 = None
    try:
        t118 = get_arg_rank_f(t12, size, F0)
    except:
        t118 = None
    try:
        t119 = fgpartition(t3)
    except:
        t119 = None
    try:
        t120 = crop(I, ORIGIN, t28)
    except:
        t120 = None
    try:
        t121 = shift(t29, DOWN)
    except:
        t121 = None
    try:
        t122 = vsplit(I, TWO)
    except:
        t122 = None
    try:
        t123 = remove(BLACK, t31)
    except:
        t123 = None
    try:
        t124 = identity(t32)
    except:
        t124 = None
    try:
        t125 = sizefilter(t7, ONE)
    except:
        t125 = None
    try:
        t126 = get_arg_rank_f(t7, size, F0)
    except:
        t126 = None
    try:
        t127 = get_nth_t(t33, F0)
    except:
        t127 = None
    try:
        t128 = fork(recolor_i, color, t34)
    except:
        t128 = None
    try:
        t129 = asobject(t35)
    except:
        t129 = None
    try:
        t130 = canvas(BLACK, t19)
    except:
        t130 = None
    try:
        t131 = recolor_i(RED, t6)
    except:
        t131 = None
    try:
        t132 = interval(TWO, NEG_ONE, NEG_ONE)
    except:
        t132 = None
    try:
        t133 = apply(double, t37)
    except:
        t133 = None
    try:
        t134 = multiply(UNITY, TEN)
    except:
        t134 = None
    if t97 == O:
        return True, f'6d0aefbc - t97'
    try:
        t135 = get_nth_f(t29, F0)
    except:
        t135 = None
    try:
        t136 = canvas(FIVE, t39)
    except:
        t136 = None
    try:
        t137 = canvas(BLACK, t40)
    except:
        t137 = None
    try:
        t138 = rbind(get_nth_t, F2)
    except:
        t138 = None
    try:
        t139 = fork(recolor_i, color, t41)
    except:
        t139 = None
    try:
        t140 = vline_i(t42)
    except:
        t140 = None
    try:
        t141 = vconcat(I, t43)
    except:
        t141 = None
    if t141 == O:
        return True, f'6fa7a44f - t141'
    try:
        t142 = colorfilter(t7, GRAY)
    except:
        t142 = None
    try:
        t143 = compose(color, t10)
    except:
        t143 = None
    try:
        t144 = compose(t44, center)
    except:
        t144 = None
    try:
        t145 = rbind(colorcount_f, YELLOW)
    except:
        t145 = None
    try:
        t146 = mir_rot_t(t5, R0)
    except:
        t146 = None
    try:
        t147 = astuple(t47, ONE)
    except:
        t147 = None
    try:
        t148 = righthalf(I)
    except:
        t148 = None
    try:
        t149 = hconcat(I, t49)
    except:
        t149 = None
    try:
        t150 = size_f(t7)
    except:
        t150 = None
    try:
        t151 = branch(t51, vsplit, hsplit)
    except:
        t151 = None
    try:
        t152 = get_nth_f(t31, F0)
    except:
        t152 = None
    try:
        t153 = hconcat(t3, I)
    except:
        t153 = None
    try:
        t154 = recolor_i(GREEN, t53)
    except:
        t154 = None
    try:
        t155 = vconcat(t16, t16)
    except:
        t155 = None
    try:
        t156 = portrait_f(t54)
    except:
        t156 = None
    try:
        t157 = get_arg_rank_f(t9, size, L1)
    except:
        t157 = None
    try:
        t158 = replace(I, t2, BLACK)
    except:
        t158 = None
    try:
        t159 = subgrid(t6, I)
    except:
        t159 = None
    try:
        t160 = canvas(BLACK, t57)
    except:
        t160 = None
    try:
        t161 = compress(I)
    except:
        t161 = None
    try:
        t162 = asobject(t59)
    except:
        t162 = None
    try:
        t163 = shape_t(t48)
    except:
        t163 = None
    try:
        t164 = subgrid(t54, I)
    except:
        t164 = None
    try:
        t165 = sizefilter(t20, FOUR)
    except:
        t165 = None
    try:
        t166 = merge(t7)
    except:
        t166 = None
    try:
        t167 = col_row(t6, R1)
    except:
        t167 = None
    try:
        t168 = rbind(colorcount_f, BLUE)
    except:
        t168 = None
    try:
        t169 = palette_f(t62)
    except:
        t169 = None
    try:
        t170 = lbind(occurrences, I)
    except:
        t170 = None
    try:
        t171 = colorfilter(t7, RED)
    except:
        t171 = None
    if t127 == O:
        return True, f'2dee498d - t127'
    try:
        t172 = asindices(t35)
    except:
        t172 = None
    try:
        t173 = initset(t64)
    except:
        t173 = None
    try:
        t174 = totuple(t7)
    except:
        t174 = None
    try:
        t175 = lbind(apply, t65)
    except:
        t175 = None
    try:
        t176 = order(t66, size)
    except:
        t176 = None
    try:
        t177 = rbind(gravitate, t53)
    except:
        t177 = None
    if t97 == O:
        return True, f'c9e6f938 - t97'
    try:
        t178 = mapply(vfrontier, t6)
    except:
        t178 = None
    try:
        t179 = lefthalf(t3)
    except:
        t179 = None
    try:
        t180 = merge_f(t9)
    except:
        t180 = None
    try:
        t181 = f_ofcolor(I, BLACK)
    except:
        t181 = None
    try:
        t182 = vconcat(t43, I)
    except:
        t182 = None
    if t182 == O:
        return True, f'4c4377d9 - t182'
    try:
        t183 = multiply(t68, THREE)
    except:
        t183 = None
    try:
        t184 = get_color_rank_t(t70, L1)
    except:
        t184 = None
    try:
        t185 = decrement(t47)
    except:
        t185 = None
    try:
        t186 = get_arg_rank_f(t17, numcolors_f, F0)
    except:
        t186 = None
    try:
        t187 = get_arg_rank_f(t9, size, F0)
    except:
        t187 = None
    try:
        t188 = mir_rot_f(t73, R2)
    except:
        t188 = None
    try:
        t189 = canvas(t50, THREE_BY_THREE)
    except:
        t189 = None
    if t189 == O:
        return True, f'5582e5ca - t189'
    try:
        t190 = decrement(t19)
    except:
        t190 = None
    try:
        t191 = lbind(apply, increment)
    except:
        t191 = None
    try:
        t192 = size_f(t9)
    except:
        t192 = None
    try:
        t193 = rbind(get_arg_rank, L1)
    except:
        t193 = None
    try:
        t194 = compose(invert, size)
    except:
        t194 = None
    try:
        t195 = fork(multiply, height_f, width_f)
    except:
        t195 = None
    try:
        t196 = sizefilter(t9, ONE)
    except:
        t196 = None
    try:
        t197 = tophalf(t48)
    except:
        t197 = None
    try:
        t198 = astuple(TWO, t74)
    except:
        t198 = None
    try:
        t199 = lbind(hupscale, t75)
    except:
        t199 = None
    try:
        t200 = cover(I, t54)
    except:
        t200 = None
    try:
        t201 = sfilter_f(t76, hline_o)
    except:
        t201 = None
    try:
        t202 = rbind(shift, NEG_UNITY)
    except:
        t202 = None
    try:
        t203 = corner(t62, R0)
    except:
        t203 = None
    try:
        t204 = o_g(t22, R5)
    except:
        t204 = None
    try:
        t205 = get_arg_rank(t12, numcolors_f, L1)
    except:
        t205 = None
    try:
        t206 = colorfilter(t8, BLUE)
    except:
        t206 = None
    try:
        t207 = colorfilter(t8, BLACK)
    except:
        t207 = None
    try:
        t208 = colorfilter(t7, BLUE)
    except:
        t208 = None
    try:
        t209 = sizefilter(t8, ONE)
    except:
        t209 = None
    try:
        t210 = switch(t77, EIGHT, NINE)
    except:
        t210 = None
    try:
        t211 = vupscale(t78, THREE)
    except:
        t211 = None
    try:
        t212 = sizefilter(t17, TWO)
    except:
        t212 = None
    try:
        t213 = prapply(connect, t79, t79)
    except:
        t213 = None
    try:
        t214 = matcher(size, BLUE)
    except:
        t214 = None
    try:
        t215 = compose(toindices, normalize)
    except:
        t215 = None
    try:
        t216 = o_g(t52, R7)
    except:
        t216 = None
    try:
        t217 = matcher(numcolors_f, RED)
    except:
        t217 = None
    try:
        t218 = chain(size, dedupe, t10)
    except:
        t218 = None
    try:
        t219 = mapply(toindices, t7)
    except:
        t219 = None
    try:
        t220 = replace(t82, ORANGE, BLACK)
    except:
        t220 = None
    try:
        t221 = get_arg_rank_f(t8, size, L1)
    except:
        t221 = None
    try:
        t222 = matcher(t10, TWO)
    except:
        t222 = None
    try:
        t223 = get_arg_rank_f(t12, size, L1)
    except:
        t223 = None
    try:
        t224 = crop(I, t83, THREE_BY_THREE)
    except:
        t224 = None
    if t224 == O:
        return True, f'5bd6f4ac - t224'
    try:
        t225 = recolor_i(BLACK, t6)
    except:
        t225 = None
    try:
        t226 = get_color_rank_t(t11, L1)
    except:
        t226 = None
    try:
        t227 = astuple(t74, t74)
    except:
        t227 = None
    try:
        t228 = halve(t47)
    except:
        t228 = None
    try:
        t229 = portrait_f(t6)
    except:
        t229 = None
    try:
        t230 = subgrid(t79, I)
    except:
        t230 = None
    try:
        t231 = halve(t74)
    except:
        t231 = None
    try:
        t232 = rbind(toobject, I)
    except:
        t232 = None
    try:
        t233 = rbind(f_ofcolor, BLACK)
    except:
        t233 = None
    try:
        t234 = compose(normalize, asobject)
    except:
        t234 = None
    try:
        t235 = matcher(color, GRAY)
    except:
        t235 = None
    try:
        t236 = replace(I, BLACK, t2)
    except:
        t236 = None
    try:
        t237 = lbind(sfilter, t7)
    except:
        t237 = None
    try:
        t238 = canvas(BLACK, t87)
    except:
        t238 = None
    try:
        t239 = mir_rot_t(t35, R4)
    except:
        t239 = None
    try:
        t240 = lbind(remove, BLACK)
    except:
        t240 = None
    try:
        t241 = get_arg_rank_f(t12, numcolors_f, L1)
    except:
        t241 = None
    try:
        t242 = replace(I, t50, THREE)
    except:
        t242 = None
    try:
        t243 = downscale(t27, TWO)
    except:
        t243 = None
    try:
        t244 = lbind(f_ofcolor, I)
    except:
        t244 = None
    try:
        t245 = branch(t51, tophalf, lefthalf)
    except:
        t245 = None
    if t141 == O:
        return True, f'8be77c9e - t141'
    try:
        t246 = c_zo_n(S, t1, t89)
    except:
        t246 = None
    try:
        t247 = c_iz_n(S, t1, t90)
    except:
        t247 = None
    try:
        t248 = center(t91)
    except:
        t248 = None
    try:
        t249 = fork(recolor_i, color, t93)
    except:
        t249 = None
    try:
        t250 = canvas(BLACK, t94)
    except:
        t250 = None
    try:
        t251 = c_iz_n(S, t1, t89)
    except:
        t251 = None
    try:
        t252 = hfrontier(t95)
    except:
        t252 = None
    try:
        t253 = color(t96)
    except:
        t253 = None
    try:
        t254 = mir_rot_t(t97, R0)
    except:
        t254 = None
    try:
        t255 = subgrid(t98, I)
    except:
        t255 = None
    try:
        t256 = move(I, t99, DOWN)
    except:
        t256 = None
    if t256 == O:
        return True, f'25ff71a9 - t256'
    try:
        t257 = compose(t10, delta)
    except:
        t257 = None
    try:
        t258 = order(t20, height_f)
    except:
        t258 = None
    try:
        t259 = canvas(BLACK, t101)
    except:
        t259 = None
    try:
        t260 = subgrid(t102, I)
    except:
        t260 = None
    try:
        t261 = upscale_t(I, t103)
    except:
        t261 = None
    if t261 == O:
        return True, f'b91ae062 - t261'
    try:
        t262 = fork(recolor_i, color, t104)
    except:
        t262 = None
    try:
        t263 = chain(t15, t105, merge)
    except:
        t263 = None
    try:
        t264 = c_zo_n(S, t1, t90)
    except:
        t264 = None
    try:
        t265 = equality(t11, t5)
    except:
        t265 = None
    try:
        t266 = subgrid(t99, I)
    except:
        t266 = None
    try:
        t267 = vconcat(t107, t107)
    except:
        t267 = None
    try:
        t268 = cover(I, t108)
    except:
        t268 = None
    try:
        t269 = get_arg_rank_f(t8, width_f, L1)
    except:
        t269 = None
    try:
        t270 = lbind(apply, t10)
    except:
        t270 = None
    try:
        t271 = lefthalf(t5)
    except:
        t271 = None
    try:
        t272 = shoot(t110, UNITY)
    except:
        t272 = None
    try:
        t273 = normalize(t91)
    except:
        t273 = None
    try:
        t274 = canvas(BLACK, t111)
    except:
        t274 = None
    try:
        t275 = cover(I, t112)
    except:
        t275 = None
    try:
        t276 = lbind(rbind, subtract)
    except:
        t276 = None
    try:
        t277 = hperiod(t114)
    except:
        t277 = None
    try:
        t278 = compose(t23, t10)
    except:
        t278 = None
    try:
        t279 = merge_f(t115)
    except:
        t279 = None
    try:
        t280 = subgrid(t116, I)
    except:
        t280 = None
    try:
        t281 = fork(connect, t10, t23)
    except:
        t281 = None
    try:
        t282 = subgrid(t118, I)
    except:
        t282 = None
    try:
        t283 = order(t119, size)
    except:
        t283 = None
    try:
        t284 = mir_rot_t(t120, R0)
    except:
        t284 = None
    try:
        t285 = fill(I, CYAN, t121)
    except:
        t285 = None
    try:
        t286 = mapply(t30, t122)
    except:
        t286 = None
    try:
        t287 = mir_rot_t(I, t124)
    except:
        t287 = None
    if t287 == O:
        return True, f'68b16354 - t287'
    try:
        t288 = merge_f(t125)
    except:
        t288 = None
    try:
        t289 = subgrid(t126, I)
    except:
        t289 = None
    if t289 == O:
        return True, f'be94b721 - t289'
    try:
        t290 = remove_t(t127, t33)
    except:
        t290 = None
    try:
        t291 = lbind(shift, t129)
    except:
        t291 = None
    try:
        t292 = apply(tojvec, t132)
    except:
        t292 = None
    try:
        t293 = apply(decrement, t133)
    except:
        t293 = None
    try:
        t294 = subgrid(t91, I)
    except:
        t294 = None
    if t294 == O:
        return True, f'c909285e - t294'
    try:
        t295 = subgrid(t114, I)
    except:
        t295 = None
    try:
        t296 = canvas(t38, t134)
    except:
        t296 = None
    try:
        t297 = shoot(t135, UP_RIGHT)
    except:
        t297 = None
    try:
        t298 = rbind(corner, R0)
    except:
        t298 = None
    try:
        t299 = rbind(shoot, UNITY)
    except:
        t299 = None
    try:
        t300 = c_zo_n(S, t1, t138)
    except:
        t300 = None
    try:
        t301 = difference(t7, t125)
    except:
        t301 = None
    try:
        t302 = rbind(col_row, R1)
    except:
        t302 = None
    try:
        t303 = subgrid(t106, I)
    except:
        t303 = None
    try:
        t304 = fork(equality, toindices, box)
    except:
        t304 = None
    try:
        t305 = fork(recolor_i, color, t144)
    except:
        t305 = None
    try:
        t306 = matcher(t145, BLACK)
    except:
        t306 = None
    try:
        t307 = col_row(t54, R1)
    except:
        t307 = None
    try:
        t308 = vconcat(t146, t5)
    except:
        t308 = None
    if t308 == O:
        return True, f'f25ffba3 - t308'
    try:
        t309 = switch(t22, ONE, TWO)
    except:
        t309 = None
    try:
        t310 = crop(I, ORIGIN, t147)
    except:
        t310 = None
    try:
        t311 = mir_rot_t(t148, R2)
    except:
        t311 = None
    try:
        t312 = astuple(t150, t150)
    except:
        t312 = None
    try:
        t313 = apply(size, t20)
    except:
        t313 = None
    try:
        t314 = sfilter_f(t76, vline_o)
    except:
        t314 = None
    try:
        t315 = t151(I, TWO)
    except:
        t315 = None
    try:
        t316 = get_nth_f(t31, L1)
    except:
        t316 = None
    try:
        t317 = mir_rot_t(t153, R0)
    except:
        t317 = None
    try:
        t318 = shift(t91, UP)
    except:
        t318 = None
    try:
        t319 = apply(t46, t22)
    except:
        t319 = None
    try:
        t320 = corner(t157, R0)
    except:
        t320 = None
    try:
        t321 = fork(equality, t18, identity)
    except:
        t321 = None
    try:
        t322 = get_color_rank_t(t158, L1)
    except:
        t322 = None
    try:
        t323 = palette_t(t161)
    except:
        t323 = None
    try:
        t324 = lbind(shift, t162)
    except:
        t324 = None
    try:
        t325 = canvas(BLACK, t163)
    except:
        t325 = None
    try:
        t326 = trim(t164)
    except:
        t326 = None
    try:
        t327 = get_nth_f(t165, F0)
    except:
        t327 = None
    try:
        t328 = lbind(shift, t166)
    except:
        t328 = None
    try:
        t329 = mapply(t60, t20)
    except:
        t329 = None
    try:
        t330 = get_arg_rank_f(t17, t168, F0)
    except:
        t330 = None
    try:
        t331 = rbind(greater, RED)
    except:
        t331 = None
    try:
        t332 = mapply(t63, t7)
    except:
        t332 = None
    if t294 == O:
        return True, f'1f85a75f - t294'
    try:
        t333 = get_nth_f(t171, F0)
    except:
        t333 = None
    try:
        t334 = chain(ineighbors, t23, t10)
    except:
        t334 = None
    try:
        t335 = recolor_i(ZERO, t172)
    except:
        t335 = None
    try:
        t336 = upscale_f(t173, THREE)
    except:
        t336 = None
    try:
        t337 = size_t(t174)
    except:
        t337 = None
    try:
        t338 = apply(t60, t20)
    except:
        t338 = None
    try:
        t339 = apply(color, t176)
    except:
        t339 = None
    try:
        t340 = lbind(compose, toindices)
    except:
        t340 = None
    try:
        t341 = fork(add, center, t177)
    except:
        t341 = None
    try:
        t342 = rbind(col_row, R2)
    except:
        t342 = None
    try:
        t343 = fill(I, RED, t178)
    except:
        t343 = None
    try:
        t344 = totuple(t9)
    except:
        t344 = None
    try:
        t345 = branch(t51, t18, identity)
    except:
        t345 = None
    try:
        t346 = righthalf(t3)
    except:
        t346 = None
    try:
        t347 = cover(I, t106)
    except:
        t347 = None
    try:
        t348 = cover(I, t180)
    except:
        t348 = None
    try:
        t349 = lbind(shift, t181)
    except:
        t349 = None
    try:
        t350 = multiply(t183, t68)
    except:
        t350 = None
    try:
        t351 = subgrid(t180, I)
    except:
        t351 = None
    try:
        t352 = normalize(t186)
    except:
        t352 = None
    try:
        t353 = rbind(f_ofcolor, t2)
    except:
        t353 = None
    try:
        t354 = remove_f(t187, t9)
    except:
        t354 = None
    try:
        t355 = fork(remove, t23, identity)
    except:
        t355 = None
    if t294 == O:
        return True, f'0b148d64 - t294'
    try:
        t356 = o_g(t11, R5)
    except:
        t356 = None
    try:
        t357 = toindices(t114)
    except:
        t357 = None
    try:
        t358 = index(I, t190)
    except:
        t358 = None
    try:
        t359 = greater(t192, FOUR)
    except:
        t359 = None
    try:
        t360 = order(t8, t194)
    except:
        t360 = None
    try:
        t361 = get_arg_rank_f(t7, t195, F0)
    except:
        t361 = None
    try:
        t362 = merge_f(t196)
    except:
        t362 = None
    try:
        t363 = crop(I, ORIGIN, t198)
    except:
        t363 = None
    try:
        t364 = compose(t199, height_t)
    except:
        t364 = None
    try:
        t365 = size_f(t201)
    except:
        t365 = None
    try:
        t366 = subgrid(t187, I)
    except:
        t366 = None
    try:
        t367 = multiply(t150, FIVE)
    except:
        t367 = None
    try:
        t368 = compose(t10, t23)
    except:
        t368 = None
    try:
        t369 = rbind(f_ofcolor, ONE)
    except:
        t369 = None
    try:
        t370 = height_f(t62)
    except:
        t370 = None
    try:
        t371 = get_arg_rank_f(t204, size, L1)
    except:
        t371 = None
    try:
        t372 = normalize(t205)
    except:
        t372 = None
    try:
        t373 = portrait_f(t106)
    except:
        t373 = None
    if t261 == O:
        return True, f'ac0a08a4 - t261'
    try:
        t374 = compose(size, delta)
    except:
        t374 = None
    try:
        t375 = rbind(bordering, I)
    except:
        t375 = None
    try:
        t376 = sizefilter(t208, FOUR)
    except:
        t376 = None
    try:
        t377 = lbind(extract, t7)
    except:
        t377 = None
    try:
        t378 = get_nth_f(t209, F0)
    except:
        t378 = None
    try:
        t379 = order(t9, size)
    except:
        t379 = None
    try:
        t380 = switch(t210, TWO, SIX)
    except:
        t380 = None
    try:
        t381 = merge_f(t174)
    except:
        t381 = None
    try:
        t382 = cellwise(I, t3, t2)
    except:
        t382 = None
    try:
        t383 = lbind(contained, RED)
    except:
        t383 = None
    try:
        t384 = fork(either, vline_i, hline_i)
    except:
        t384 = None
    try:
        t385 = fill(I, BLACK, t96)
    except:
        t385 = None
    try:
        t386 = lbind(shift, t99)
    except:
        t386 = None
    try:
        t387 = extract(t9, t214)
    except:
        t387 = None
    try:
        t388 = lbind(shift, t180)
    except:
        t388 = None
    try:
        t389 = colorfilter(t216, TWO)
    except:
        t389 = None
    try:
        t390 = extract(t12, t217)
    except:
        t390 = None
    try:
        t391 = t218(I)
    except:
        t391 = None
    try:
        t392 = decrement(t74)
    except:
        t392 = None
    try:
        t393 = delta(t219)
    except:
        t393 = None
    try:
        t394 = lbind(rbind, gravitate)
    except:
        t394 = None
    try:
        t395 = remove_f(t221, t8)
    except:
        t395 = None
    try:
        t396 = lbind(other, t123)
    except:
        t396 = None
    try:
        t397 = colorfilter(t7, t2)
    except:
        t397 = None
    try:
        t398 = rbind(sfilter, t222)
    except:
        t398 = None
    try:
        t399 = subgrid(t223, I)
    except:
        t399 = None
    try:
        t400 = rbind(get_nth_t, F4)
    except:
        t400 = None
    try:
        t401 = normalize(t225)
    except:
        t401 = None
    try:
        t402 = get_arg_rank_f(t207, size, L1)
    except:
        t402 = None
    try:
        t403 = move(I, t96, DOWN)
    except:
        t403 = None
    try:
        t404 = hfrontier(TWO_BY_ZERO)
    except:
        t404 = None
    try:
        t405 = canvas(BLACK, t227)
    except:
        t405 = None
    try:
        t406 = cover(I, t91)
    except:
        t406 = None
    try:
        t407 = lbind(shift, t187)
    except:
        t407 = None
    try:
        t408 = mir_rot_f(t180, R0)
    except:
        t408 = None
    try:
        t409 = vupscale(I, t231)
    except:
        t409 = None
    try:
        t410 = chain(t85, t232, delta)
    except:
        t410 = None
    try:
        t411 = compose(size, t233)
    except:
        t411 = None
    try:
        t412 = extract(t20, t235)
    except:
        t412 = None
    try:
        t413 = get_color_rank_t(t236, L1)
    except:
        t413 = None
    try:
        t414 = compose(size, t237)
    except:
        t414 = None
    try:
        t415 = mir_rot_t(t35, R5)
    except:
        t415 = None
    if t294 == O:
        return True, f'23b5c85d - t294'
    try:
        t416 = prapply(connect, t6, t54)
    except:
        t416 = None
    try:
        t417 = matcher(t10, GRAY)
    except:
        t417 = None
    try:
        t418 = chain(t10, t240, palette_f)
    except:
        t418 = None
    try:
        t419 = other_f(t12, t241)
    except:
        t419 = None
    try:
        t420 = mir_rot_t(t243, R5)
    except:
        t420 = None
    try:
        t421 = fork(t88, t244, t244)
    except:
        t421 = None
    try:
        t422 = difference(t8, t207)
    except:
        t422 = None
    try:
        t423 = t245(I)
    except:
        t423 = None
    if t423 == O:
        return True, f'7b7f7511 - t423'
    try:
        t424 = fork(equality, size, t195)
    except:
        t424 = None
    try:
        t425 = lbind(mapply, hfrontier)
    except:
        t425 = None
    try:
        t426 = corner(t91, R0)
    except:
        t426 = None
    try:
        t427 = f_ofcolor(I, t251)
    except:
        t427 = None
    try:
        t428 = fill(I, RED, t252)
    except:
        t428 = None
    try:
        t429 = vconcat(t97, t254)
    except:
        t429 = None
    if t429 == O:
        return True, f'67e8384a - t429'
    try:
        t430 = height_t(t255)
    except:
        t430 = None
    try:
        t431 = fork(gravitate, t10, t23)
    except:
        t431 = None
    try:
        t432 = rbind(colorcount_f, t2)
    except:
        t432 = None
    try:
        t433 = get_nth_t(t258, L1)
    except:
        t433 = None
    try:
        t434 = replace(I, t247, BLACK)
    except:
        t434 = None
    try:
        t435 = compose(backdrop, inbox)
    except:
        t435 = None
    try:
        t436 = mir_rot_t(t260, R0)
    except:
        t436 = None
    try:
        t437 = replace(I, t251, BLACK)
    except:
        t437 = None
    try:
        t438 = rbind(col_row, R3)
    except:
        t438 = None
    try:
        t439 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    except:
        t439 = None
    try:
        t440 = hconcat(t266, t266)
    except:
        t440 = None
    if t440 == O:
        return True, f'28bf18c6 - t440'
    try:
        t441 = vconcat(t267, t107)
    except:
        t441 = None
    try:
        t442 = rbind(subgrid, t268)
    except:
        t442 = None
    try:
        t443 = size_f(t269)
    except:
        t443 = None
    try:
        t444 = f_ofcolor(t271, CYAN)
    except:
        t444 = None
    try:
        t445 = fill(I, RED, t272)
    except:
        t445 = None
    try:
        t446 = shift(t273, NEG_UNITY)
    except:
        t446 = None
    try:
        t447 = tojvec(t277)
    except:
        t447 = None
    try:
        t448 = power(t23, TWO)
    except:
        t448 = None
    try:
        t449 = cover(I, t279)
    except:
        t449 = None
    try:
        t450 = trim(t280)
    except:
        t450 = None
    if t450 == O:
        return True, f'1c786137 - t450'
    try:
        t451 = fork(multiply, sign, identity)
    except:
        t451 = None
    try:
        t452 = get_nth_t(t283, L1)
    except:
        t452 = None
    try:
        t453 = hconcat(t120, t284)
    except:
        t453 = None
    try:
        t454 = lefthalf(t260)
    except:
        t454 = None
    try:
        t455 = get_arg_rank_t(t286, numcolors_t, F0)
    except:
        t455 = None
    if t455 == O:
        return True, f'2dc579da - t455'
    try:
        t456 = cover(I, t288)
    except:
        t456 = None
    try:
        t457 = get_nth_t(t290, L1)
    except:
        t457 = None
    try:
        t458 = compose(t291, decrement)
    except:
        t458 = None
    try:
        t459 = corner(t53, R0)
    except:
        t459 = None
    try:
        t460 = rbind(apply, t292)
    except:
        t460 = None
    try:
        t461 = papply(astuple, t293, t293)
    except:
        t461 = None
    try:
        t462 = get_color_rank_t(t295, L1)
    except:
        t462 = None
    try:
        t463 = fill(I, BLUE, t297)
    except:
        t463 = None
    try:
        t464 = center(t96)
    except:
        t464 = None
    try:
        t465 = asindices(t136)
    except:
        t465 = None
    try:
        t466 = compose(t299, center)
    except:
        t466 = None
    try:
        t467 = get_nth_f(t301, F0)
    except:
        t467 = None
    try:
        t468 = mir_rot_t(t260, R2)
    except:
        t468 = None
    if t468 == O:
        return True, f'7468f01a - t468'
    try:
        t469 = o_g(t148, R5)
    except:
        t469 = None
    try:
        t470 = rbind(shoot, UP)
    except:
        t470 = None
    try:
        t471 = upscale_t(t303, THREE)
    except:
        t471 = None
    try:
        t472 = extract(t142, t304)
    except:
        t472 = None
    try:
        t473 = extract(t17, t306)
    except:
        t473 = None
    try:
        t474 = lbind(greater, t307)
    except:
        t474 = None
    try:
        t475 = fork(recolor_o, t143, t23)
    except:
        t475 = None
    try:
        t476 = apply(t46, t309)
    except:
        t476 = None
    try:
        t477 = o_g(t311, R5)
    except:
        t477 = None
    try:
        t478 = canvas(BLACK, t312)
    except:
        t478 = None
    try:
        t479 = contained(ONE, t313)
    except:
        t479 = None
    try:
        t480 = difference(t76, t314)
    except:
        t480 = None
    try:
        t481 = canvas(t246, THREE_BY_THREE)
    except:
        t481 = None
    try:
        t482 = get_arg_rank_t(t315, numcolors_t, F0)
    except:
        t482 = None
    try:
        t483 = switch(I, t152, t316)
    except:
        t483 = None
    if t429 == O:
        return True, f'3af2c5a8 - t429'
    try:
        t484 = vconcat(t317, t153)
    except:
        t484 = None
    if t484 == O:
        return True, f'0c786b71 - t484'
    try:
        t485 = corner(t318, R0)
    except:
        t485 = None
    try:
        t486 = get_nth_f(t79, F0)
    except:
        t486 = None
    try:
        t487 = mir_rot_t(t319, R4)
    except:
        t487 = None
    if t487 == O:
        return True, f'1e0a9b12 - t487'
    try:
        t488 = branch(t156, identity, t18)
    except:
        t488 = None
    try:
        t489 = index(I, t320)
    except:
        t489 = None
    if t429 == O:
        return True, f'62c24649 - t429'
    try:
        t490 = difference(t8, t209)
    except:
        t490 = None
    try:
        t491 = compose(flip, t321)
    except:
        t491 = None
    try:
        t492 = upscale_t(t266, THREE)
    except:
        t492 = None
    try:
        t493 = lbind(colorcount_t, t161)
    except:
        t493 = None
    try:
        t494 = occurrences(I, t162)
    except:
        t494 = None
    try:
        t495 = get_color_rank_t(t326, L1)
    except:
        t495 = None
    try:
        t496 = subgrid(t327, I)
    except:
        t496 = None
    try:
        t497 = shape_f(t166)
    except:
        t497 = None
    try:
        t498 = paint(I, t329)
    except:
        t498 = None
    if t498 == O:
        return True, f'56ff96f3 - t498'
    try:
        t499 = col_row(t53, R1)
    except:
        t499 = None
    try:
        t500 = subgrid(t330, I)
    except:
        t500 = None
    if t500 == O:
        return True, f'ae4f1146 - t500'
    try:
        t501 = rbind(upscale_f, RED)
    except:
        t501 = None
    try:
        t502 = compose(invert, t298)
    except:
        t502 = None
    try:
        t503 = subtract(t47, TWO)
    except:
        t503 = None
    try:
        t504 = rbind(difference, t91)
    except:
        t504 = None
    try:
        t505 = fill(I, BLACK, t332)
    except:
        t505 = None
    if t505 == O:
        return True, f'4347f46a - t505'
    try:
        t506 = lbind(matcher, t10)
    except:
        t506 = None
    try:
        t507 = astuple(FOUR, FOUR)
    except:
        t507 = None
    try:
        t508 = colorfilter(t7, CYAN)
    except:
        t508 = None
    try:
        t509 = dedupe(t295)
    except:
        t509 = None
    try:
        t510 = fork(recolor_i, color, t334)
    except:
        t510 = None
    try:
        t511 = height_f(t53)
    except:
        t511 = None
    try:
        t512 = order(t315, numcolors_t)
    except:
        t512 = None
    try:
        t513 = lbind(shift, t335)
    except:
        t513 = None
    try:
        t514 = toindices(t336)
    except:
        t514 = None
    try:
        t515 = interval(t337, ZERO, NEG_ONE)
    except:
        t515 = None
    try:
        t516 = mfilter_f(t338, hline_o)
    except:
        t516 = None
    try:
        t517 = get_nth_t(t176, L1)
    except:
        t517 = None
    try:
        t518 = rbind(compose, t10)
    except:
        t518 = None
    try:
        t519 = fork(connect, center, t341)
    except:
        t519 = None
    try:
        t520 = order(t7, t342)
    except:
        t520 = None
    try:
        t521 = rbind(add, DOWN)
    except:
        t521 = None
    try:
        t522 = apply(t55, t344)
    except:
        t522 = None
    try:
        t523 = t345(I)
    except:
        t523 = None
    try:
        t524 = mir_rot_t(t346, R2)
    except:
        t524 = None
    try:
        t525 = chain(toivec, invert, height_f)
    except:
        t525 = None
    try:
        t526 = other_f(t123, t2)
    except:
        t526 = None
    try:
        t527 = subtract(t350, THREE)
    except:
        t527 = None
    try:
        t528 = f_ofcolor(t70, t184)
    except:
        t528 = None
    try:
        t529 = astuple(t185, t74)
    except:
        t529 = None
    try:
        t530 = lbind(shift, t352)
    except:
        t530 = None
    try:
        t531 = merge_f(t354)
    except:
        t531 = None
    try:
        t532 = compose(t72, t355)
    except:
        t532 = None
    try:
        t533 = corner(t79, R0)
    except:
        t533 = None
    try:
        t534 = merge_f(t356)
    except:
        t534 = None
    try:
        t535 = contained(TWO_BY_ZERO, t357)
    except:
        t535 = None
    try:
        t536 = double(t19)
    except:
        t536 = None
    try:
        t537 = compose(t23, t23)
    except:
        t537 = None
    try:
        t538 = apply(color, t360)
    except:
        t538 = None
    try:
        t539 = color(t361)
    except:
        t539 = None
    try:
        t540 = cover(I, t362)
    except:
        t540 = None
    if t540 == O:
        return True, f'42a50994 - t540'
    try:
        t541 = fork(difference, asindices, t233)
    except:
        t541 = None
    try:
        t542 = tophalf(t363)
    except:
        t542 = None
    try:
        t543 = rbind(hconcat, t75)
    except:
        t543 = None
    try:
        t544 = positive(t365)
    except:
        t544 = None
    try:
        t545 = get_color_rank_t(t366, L1)
    except:
        t545 = None
    try:
        t546 = astuple(t367, t367)
    except:
        t546 = None
    try:
        t547 = lbind(add, RIGHT)
    except:
        t547 = None
    try:
        t548 = compose(normalize, t369)
    except:
        t548 = None
    try:
        t549 = hperiod(t62)
    except:
        t549 = None
    try:
        t550 = color(t371)
    except:
        t550 = None
    try:
        t551 = upscale_f(t372, FOUR)
    except:
        t551 = None
    try:
        t552 = get_arg_rank_f(t206, t374, F0)
    except:
        t552 = None
    try:
        t553 = compose(flip, t375)
    except:
        t553 = None
    try:
        t554 = size_f(t376)
    except:
        t554 = None
    try:
        t555 = center(t378)
    except:
        t555 = None
    try:
        t556 = apply(color, t379)
    except:
        t556 = None
    try:
        t557 = switch(t380, ONE, FIVE)
    except:
        t557 = None
    if t557 == O:
        return True, f'b1948b0a - t557'
    try:
        t558 = subgrid(t381, I)
    except:
        t558 = None
    try:
        t559 = move(I, t288, TWO_BY_ZERO)
    except:
        t559 = None
    if t559 == O:
        return True, f'3618c87e - t559'
    try:
        t560 = mir_rot_t(t382, R0)
    except:
        t560 = None
    try:
        t561 = compose(t383, palette_f)
    except:
        t561 = None
    try:
        t562 = mfilter_f(t213, t384)
    except:
        t562 = None
    try:
        t563 = toindices(t126)
    except:
        t563 = None
    try:
        t564 = shift(t96, DOWN)
    except:
        t564 = None
    try:
        t565 = height_f(t99)
    except:
        t565 = None
    try:
        t566 = lbind(adjacent, t387)
    except:
        t566 = None
    try:
        t567 = rbind(multiply, GREEN)
    except:
        t567 = None
    try:
        t568 = product(t389, t389)
    except:
        t568 = None
    try:
        t569 = subgrid(t390, I)
    except:
        t569 = None
    try:
        t570 = equality(t391, BLUE)
    except:
        t570 = None
    try:
        t571 = tojvec(t392)
    except:
        t571 = None
    try:
        t572 = rbind(adjacent, t29)
    except:
        t572 = None
    try:
        t573 = fill(I, YELLOW, t393)
    except:
        t573 = None
    if t557 == O:
        return True, f'0d3d703e - t557'
    try:
        t574 = rbind(adjacent, t221)
    except:
        t574 = None
    try:
        t575 = compose(t396, color)
    except:
        t575 = None
    try:
        t576 = difference(t7, t397)
    except:
        t576 = None
    try:
        t577 = compose(center, t398)
    except:
        t577 = None
    try:
        t578 = identity(t400)
    except:
        t578 = None
    try:
        t579 = lbind(shift, t401)
    except:
        t579 = None
    try:
        t580 = backdrop(t402)
    except:
        t580 = None
    try:
        t581 = astuple(t228, t74)
    except:
        t581 = None
    try:
        t582 = branch(t229, identity, t18)
    except:
        t582 = None
    try:
        t583 = replace(t158, t322, t2)
    except:
        t583 = None
    if t583 == O:
        return True, f'aabf363d - t583'
    try:
        t584 = vconcat(t153, t317)
    except:
        t584 = None
    try:
        t585 = get_color_rank_t(t406, L1)
    except:
        t585 = None
    try:
        t586 = rbind(col_row, R0)
    except:
        t586 = None
    try:
        t587 = lbind(mapply, t407)
    except:
        t587 = None
    try:
        t588 = replace(I, CYAN, t246)
    except:
        t588 = None
    try:
        t589 = paint(I, t408)
    except:
        t589 = None
    try:
        t590 = rbind(shift, UP)
    except:
        t590 = None
    try:
        t591 = corner(t412, R0)
    except:
        t591 = None
    try:
        t592 = f_ofcolor(I, t413)
    except:
        t592 = None
    try:
        t593 = t414(vline_o)
    except:
        t593 = None
    try:
        t594 = astuple(t239, t415)
    except:
        t594 = None
    try:
        t595 = mfilter_f(t416, vline_i)
    except:
        t595 = None
    try:
        t596 = upscale_t(t266, TWO)
    except:
        t596 = None
    if t596 == O:
        return True, f'f25fbde4 - t596'
    try:
        t597 = rbind(sfilter, t417)
    except:
        t597 = None
    try:
        t598 = subgrid(t419, I)
    except:
        t598 = None
    try:
        t599 = get_arg_rank_f(t7, size, L1)
    except:
        t599 = None
    try:
        t600 = upscale_t(t420, FOUR)
    except:
        t600 = None
    if t600 == O:
        return True, f'46f33fce - t600'
    try:
        t601 = compose(merge, t421)
    except:
        t601 = None
    try:
        t602 = compose(normalize, toindices)
    except:
        t602 = None
    try:
        t603 = identity(t89)
    except:
        t603 = None
    try:
        t604 = extract(t20, t424)
    except:
        t604 = None
    try:
        t605 = shift(t29, RIGHT)
    except:
        t605 = None
    try:
        t606 = subtract(t248, t426)
    except:
        t606 = None
    try:
        t607 = mapply(t249, t9)
    except:
        t607 = None
    try:
        t608 = mapply(neighbors, t54)
    except:
        t608 = None
    try:
        t609 = col_row(t96, R2)
    except:
        t609 = None
    try:
        t610 = vsplit(t255, t430)
    except:
        t610 = None
    try:
        t611 = compose(crement, t431)
    except:
        t611 = None
    try:
        t612 = matcher(t432, RED)
    except:
        t612 = None
    try:
        t613 = remove_f(t433, t258)
    except:
        t613 = None
    try:
        t614 = o_g(t436, R3)
    except:
        t614 = None
    try:
        t615 = mapply(t262, t7)
    except:
        t615 = None
    try:
        t616 = t263(t20)
    except:
        t616 = None
    try:
        t617 = rbind(t36, t438)
    except:
        t617 = None
    try:
        t618 = matcher(size, MAGENTA)
    except:
        t618 = None
    try:
        t619 = branch(t265, t5, t439)
    except:
        t619 = None
    try:
        t620 = height_f(t108)
    except:
        t620 = None
    try:
        t621 = equality(t443, BLUE)
    except:
        t621 = None
    try:
        t622 = get_arg_rank_f(t20, size, F0)
    except:
        t622 = None
    try:
        t623 = fill(t109, CYAN, t444)
    except:
        t623 = None
    try:
        t624 = lbind(shift, t446)
    except:
        t624 = None
    try:
        t625 = shift(t62, UNITY)
    except:
        t625 = None
    try:
        t626 = compose(t276, t298)
    except:
        t626 = None
    try:
        t627 = shift(t114, t447)
    except:
        t627 = None
    try:
        t628 = fork(connect, t278, t448)
    except:
        t628 = None
    try:
        t629 = apply(toindices, t9)
    except:
        t629 = None
    try:
        t630 = product(t73, t73)
    except:
        t630 = None
    try:
        t631 = colorfilter(t8, RED)
    except:
        t631 = None
    try:
        t632 = downscale(t437, THREE)
    except:
        t632 = None
    if t632 == O:
        return True, f'5614dbcf - t632'
    try:
        t633 = lbind(apply, t451)
    except:
        t633 = None
    try:
        t634 = f_ofcolor(t3, GRAY)
    except:
        t634 = None
    try:
        t635 = remove_f(t452, t283)
    except:
        t635 = None
    try:
        t636 = hconcat(t453, t453)
    except:
        t636 = None
    try:
        t637 = tophalf(t454)
    except:
        t637 = None
    if t637 == O:
        return True, f'2013d3e2 - t637'
    try:
        t638 = get_arg_rank_f(t9, t195, F0)
    except:
        t638 = None
    try:
        t639 = corner(t54, R1)
    except:
        t639 = None
    try:
        t640 = delta(t73)
    except:
        t640 = None
    try:
        t641 = get_nth_t(t290, F0)
    except:
        t641 = None
    try:
        t642 = mapply(t128, t125)
    except:
        t642 = None
    try:
        t643 = paint(t130, t126)
    except:
        t643 = None
    try:
        t644 = corner(t6, R0)
    except:
        t644 = None
    try:
        t645 = lbind(shift, t461)
    except:
        t645 = None
    try:
        t646 = get_color_rank_t(t295, F0)
    except:
        t646 = None
    try:
        t647 = other_f(t31, t251)
    except:
        t647 = None
    try:
        t648 = f_ofcolor(t463, BLUE)
    except:
        t648 = None
    try:
        t649 = lbind(shoot, t464)
    except:
        t649 = None
    try:
        t650 = box(t465)
    except:
        t650 = None
    try:
        t651 = fork(recolor_i, color, t466)
    except:
        t651 = None
    try:
        t652 = lbind(sizefilter, t7)
    except:
        t652 = None
    try:
        t653 = get_color_rank_t(t437, L1)
    except:
        t653 = None
    try:
        t654 = color(t467)
    except:
        t654 = None
    try:
        t655 = mapply(t139, t469)
    except:
        t655 = None
    try:
        t656 = branch(t140, t302, t438)
    except:
        t656 = None
    try:
        t657 = f_ofcolor(I, ORANGE)
    except:
        t657 = None
    try:
        t658 = hconcat(t303, t303)
    except:
        t658 = None
    try:
        t659 = inbox(t472)
    except:
        t659 = None
    try:
        t660 = compose(center, t23)
    except:
        t660 = None
    try:
        t661 = mapply(t305, t7)
    except:
        t661 = None
    try:
        t662 = remove_f(t473, t17)
    except:
        t662 = None
    try:
        t663 = merge_f(t76)
    except:
        t663 = None
    try:
        t664 = switch(t476, ONE, TWO)
    except:
        t664 = None
    try:
        t665 = hupscale(t310, t74)
    except:
        t665 = None
    try:
        t666 = merge_f(t477)
    except:
        t666 = None
    try:
        t667 = hconcat(t22, t27)
    except:
        t667 = None
    try:
        t668 = size_f(t20)
    except:
        t668 = None
    try:
        t669 = f_ofcolor(I, BURGUNDY)
    except:
        t669 = None
    try:
        t670 = astuple(t480, t314)
    except:
        t670 = None
    try:
        t671 = width_t(t482)
    except:
        t671 = None
    try:
        t672 = lbind(contained, t251)
    except:
        t672 = None
    try:
        t673 = shoot(t485, NEG_UNITY)
    except:
        t673 = None
    try:
        t674 = get_nth_f(t53, F0)
    except:
        t674 = None
    try:
        t675 = recolor_i(t246, t6)
    except:
        t675 = None
    try:
        t676 = equality(t489, CYAN)
    except:
        t676 = None
    try:
        t677 = apply(t55, t490)
    except:
        t677 = None
    try:
        t678 = mapply(neighbors, t53)
    except:
        t678 = None
    try:
        t679 = extract(t56, t491)
    except:
        t679 = None
    if t679 == O:
        return True, f'662c240a - t679'
    try:
        t680 = rbind(colorcount_f, t322)
    except:
        t680 = None
    try:
        t681 = width_t(t159)
    except:
        t681 = None
    try:
        t682 = sizefilter(t7, TWO)
    except:
        t682 = None
    try:
        t683 = compose(invert, t493)
    except:
        t683 = None
    try:
        t684 = mapply(t324, t494)
    except:
        t684 = None
    try:
        t685 = inbox(t54)
    except:
        t685 = None
    try:
        t686 = trim(t496)
    except:
        t686 = None
    try:
        t687 = lbind(multiply, t497)
    except:
        t687 = None
    try:
        t688 = astuple(t167, t499)
    except:
        t688 = None
    try:
        t689 = rbind(mir_rot_f, R2)
    except:
        t689 = None
    try:
        t690 = fill(I, t251, t26)
    except:
        t690 = None
    try:
        t691 = lbind(compose, t502)
    except:
        t691 = None
    try:
        t692 = divide(t503, THREE)
    except:
        t692 = None
    try:
        t693 = chain(t331, size, t504)
    except:
        t693 = None
    try:
        t694 = rbind(get_color_rank_f, F0)
    except:
        t694 = None
    try:
        t695 = prapply(connect, t73, t73)
    except:
        t695 = None
    try:
        t696 = canvas(t246, t507)
    except:
        t696 = None
    try:
        t697 = get_nth_f(t508, F0)
    except:
        t697 = None
    try:
        t698 = mir_rot_t(t509, R4)
    except:
        t698 = None
    try:
        t699 = equality(t511, BLUE)
    except:
        t699 = None
    if t637 == O:
        return True, f'73182012 - t637'
    try:
        t700 = get_nth_f(t512, F0)
    except:
        t700 = None
    try:
        t701 = initset(ZERO)
    except:
        t701 = None
    try:
        t702 = lbind(shift, t514)
    except:
        t702 = None
    try:
        t703 = order(t7, height_f)
    except:
        t703 = None
    try:
        t704 = colorfilter(t8, GREEN)
    except:
        t704 = None
    try:
        t705 = paint(I, t516)
    except:
        t705 = None
    if t705 == O:
        return True, f'22eb0ac0 - t705'
    try:
        t706 = sizefilter(t8, THREE)
    except:
        t706 = None
    try:
        t707 = repeat(t517, BLUE)
    except:
        t707 = None
    try:
        t708 = lbind(rbind, equality)
    except:
        t708 = None
    try:
        t709 = fork(recolor_i, color, t519)
    except:
        t709 = None
    try:
        t710 = apply(color, t520)
    except:
        t710 = None
    try:
        t711 = canvas(t246, t19)
    except:
        t711 = None
    try:
        t712 = f_ofcolor(t49, BLUE)
    except:
        t712 = None
    try:
        t713 = rbind(corner, R2)
    except:
        t713 = None
    try:
        t714 = rbind(mir_rot_t, R2)
    except:
        t714 = None
    try:
        t715 = branch(t51, height_t, width_t)
    except:
        t715 = None
    try:
        t716 = fork(subtract, t278, t448)
    except:
        t716 = None
    try:
        t717 = cellwise(t179, t524, ZERO)
    except:
        t717 = None
    try:
        t718 = fork(shift, identity, t525)
    except:
        t718 = None
    try:
        t719 = col_row(t29, R0)
    except:
        t719 = None
    try:
        t720 = switch(I, t2, t526)
    except:
        t720 = None
    try:
        t721 = rbind(corner, R3)
    except:
        t721 = None
    try:
        t722 = astuple(THREE, t527)
    except:
        t722 = None
    try:
        t723 = combine_f(t6, t528)
    except:
        t723 = None
    try:
        t724 = crop(I, ORIGIN, t529)
    except:
        t724 = None
    try:
        t725 = colorfilter(t17, t251)
    except:
        t725 = None
    try:
        t726 = color(t531)
    except:
        t726 = None
    try:
        t727 = fork(vconcat, identity, t532)
    except:
        t727 = None
    try:
        t728 = index(I, t533)
    except:
        t728 = None
    try:
        t729 = apply(outbox, t7)
    except:
        t729 = None
    try:
        t730 = paint(t5, t534)
    except:
        t730 = None
    if t730 == O:
        return True, f'e98196ab - t730'
    try:
        t731 = compose(vfrontier, tojvec)
    except:
        t731 = None
    try:
        t732 = canvas(t358, t536)
    except:
        t732 = None
    try:
        t733 = matcher(t23, t231)
    except:
        t733 = None
    try:
        t734 = mir_rot_f(t6, R2)
    except:
        t734 = None
    try:
        t735 = rbind(t193, t537)
    except:
        t735 = None
    try:
        t736 = order(t8, size)
    except:
        t736 = None
    try:
        t737 = canvas(t539, TWO_BY_TWO)
    except:
        t737 = None
    if t737 == O:
        return True, f'445eab21 - t737'
    try:
        t738 = fork(toobject, t541, identity)
    except:
        t738 = None
    try:
        t739 = mir_rot_t(t542, R1)
    except:
        t739 = None
    try:
        t740 = canvas(BLACK, UNITY)
    except:
        t740 = None
    try:
        t741 = outbox(t6)
    except:
        t741 = None
    try:
        t742 = fork(connect, t298, centerofmass)
    except:
        t742 = None
    try:
        t743 = replace(t366, t545, BLACK)
    except:
        t743 = None
    try:
        t744 = canvas(BLACK, t546)
    except:
        t744 = None
    try:
        t745 = chain(t21, t202, t548)
    except:
        t745 = None
    try:
        t746 = astuple(t370, t549)
    except:
        t746 = None
    try:
        t747 = canvas(t550, THREE_BY_THREE)
    except:
        t747 = None
    try:
        t748 = paint(I, t551)
    except:
        t748 = None
    try:
        t749 = branch(t373, identity, t18)
    except:
        t749 = None
    try:
        t750 = rbind(gravitate, t467)
    except:
        t750 = None
    try:
        t751 = subgrid(t552, I)
    except:
        t751 = None
    if t751 == O:
        return True, f'8efcae92 - t751'
    try:
        t752 = extract(t207, t553)
    except:
        t752 = None
    try:
        t753 = astuple(ONE, t554)
    except:
        t753 = None
    try:
        t754 = matcher(t67, BLACK)
    except:
        t754 = None
    try:
        t755 = colorfilter(t7, MAGENTA)
    except:
        t755 = None
    try:
        t756 = neighbors(t555)
    except:
        t756 = None
    try:
        t757 = apply(t58, t556)
    except:
        t757 = None
    try:
        t758 = remove(t251, t31)
    except:
        t758 = None
    try:
        t759 = apply(initset, t26)
    except:
        t759 = None
    try:
        t760 = cellwise(t382, t560, t2)
    except:
        t760 = None
    try:
        t761 = mfilter_f(t212, t561)
    except:
        t761 = None
    try:
        t762 = underfill(I, NEG_ONE, t562)
    except:
        t762 = None
    try:
        t763 = paint(t385, t564)
    except:
        t763 = None
    try:
        t764 = rbind(multiply, t565)
    except:
        t764 = None
    try:
        t765 = astuple(NINE, t74)
    except:
        t765 = None
    try:
        t766 = extract(t9, t566)
    except:
        t766 = None
    try:
        t767 = apply(delta, t7)
    except:
        t767 = None
    try:
        t768 = mapply(dneighbors, t29)
    except:
        t768 = None
    try:
        t769 = neighbors(ORIGIN)
    except:
        t769 = None
    try:
        t770 = sfilter_f(t8, square_f)
    except:
        t770 = None
    try:
        t771 = f_ofcolor(t35, BLACK)
    except:
        t771 = None
    try:
        t772 = height_f(t427)
    except:
        t772 = None
    try:
        t773 = lbind(greater, FIVE)
    except:
        t773 = None
    try:
        t774 = get_nth_f(t6, F0)
    except:
        t774 = None
    try:
        t775 = mapply(delta, t9)
    except:
        t775 = None
    try:
        t776 = shoot(t571, DOWN_LEFT)
    except:
        t776 = None
    try:
        t777 = mfilter_f(t207, t572)
    except:
        t777 = None
    try:
        t778 = order(t7, t194)
    except:
        t778 = None
    try:
        t779 = extract(t395, t574)
    except:
        t779 = None
    try:
        t780 = fork(recolor_i, t575, outbox)
    except:
        t780 = None
    try:
        t781 = get_arg_rank_f(t576, size, F0)
    except:
        t781 = None
    try:
        t782 = c_zo_n(t84, t1, t578)
    except:
        t782 = None
    try:
        t783 = box(t29)
    except:
        t783 = None
    try:
        t784 = occurrences(I, t225)
    except:
        t784 = None
    try:
        t785 = toobject(t580, I)
    except:
        t785 = None
    try:
        t786 = box(t26)
    except:
        t786 = None
    try:
        t787 = crop(I, ORIGIN, t581)
    except:
        t787 = None
    try:
        t788 = col_row(t6, R2)
    except:
        t788 = None
    try:
        t789 = vconcat(t584, t153)
    except:
        t789 = None
    try:
        t790 = f_ofcolor(t406, t585)
    except:
        t790 = None
    try:
        t791 = get_arg_rank_f(t12, t586, F0)
    except:
        t791 = None
    try:
        t792 = double(TEN)
    except:
        t792 = None
    try:
        t793 = mir_rot_f(t180, R2)
    except:
        t793 = None
    try:
        t794 = other_f(t31, BLACK)
    except:
        t794 = None
    try:
        t795 = compose(t590, backdrop)
    except:
        t795 = None
    try:
        t796 = subtract(t591, DOWN)
    except:
        t796 = None
    try:
        t797 = mapply(dneighbors, t592)
    except:
        t797 = None
    try:
        t798 = t414(hline_o)
    except:
        t798 = None
    try:
        t799 = get_nth_f(t91, F0)
    except:
        t799 = None
    try:
        t800 = delta(t54)
    except:
        t800 = None
    try:
        t801 = apply(asobject, t594)
    except:
        t801 = None
    try:
        t802 = underfill(I, RED, t595)
    except:
        t802 = None
    try:
        t803 = chain(invert, center, t597)
    except:
        t803 = None
    try:
        t804 = chain(t418, t232, outbox)
    except:
        t804 = None
    try:
        t805 = hline_o(t599)
    except:
        t805 = None
    try:
        t806 = fork(recolor_i, identity, t601)
    except:
        t806 = None
    try:
        t807 = c_zo_n(t84, t1, t603)
    except:
        t807 = None
    try:
        t808 = other_f(t20, t604)
    except:
        t808 = None
    try:
        t809 = replace(I, t247, t251)
    except:
        t809 = None
    try:
        t810 = shift(t29, LEFT)
    except:
        t810 = None
    try:
        t811 = lbind(multiply, t606)
    except:
        t811 = None
    try:
        t812 = paint(I, t607)
    except:
        t812 = None
    try:
        t813 = fill(I, t246, t608)
    except:
        t813 = None
    if t813 == O:
        return True, f'4258a5f9 - t813'
    try:
        t814 = center(t73)
    except:
        t814 = None
    try:
        t815 = interval(t609, TEN, TWO)
    except:
        t815 = None
    try:
        t816 = lbind(greater, YELLOW)
    except:
        t816 = None
    try:
        t817 = fork(add, t100, t611)
    except:
        t817 = None
    try:
        t818 = get_nth_t(t613, L1)
    except:
        t818 = None
    try:
        t819 = mapply(t435, t7)
    except:
        t819 = None
    try:
        t820 = get_nth_f(t614, F0)
    except:
        t820 = None
    try:
        t821 = paint(I, t615)
    except:
        t821 = None
    if t821 == O:
        return True, f'd037b0a7 - t821'
    try:
        t822 = upscale_f(t616, THREE)
    except:
        t822 = None
    try:
        t823 = lbind(colorfilter, t7)
    except:
        t823 = None
    try:
        t824 = mfilter_f(t7, t618)
    except:
        t824 = None
    try:
        t825 = vconcat(I, t619)
    except:
        t825 = None
    try:
        t826 = equality(t620, FIVE)
    except:
        t826 = None
    try:
        t827 = branch(t621, identity, outbox)
    except:
        t827 = None
    try:
        t828 = remove_f(t622, t20)
    except:
        t828 = None
    try:
        t829 = corner(t29, R0)
    except:
        t829 = None
    try:
        t830 = inbox(t91)
    except:
        t830 = None
    try:
        t831 = paint(t274, t625)
    except:
        t831 = None
    try:
        t832 = prapply(connect, t91, t91)
    except:
        t832 = None
    try:
        t833 = astuple(TWO, FOUR)
    except:
        t833 = None
    try:
        t834 = paint(I, t627)
    except:
        t834 = None
    try:
        t835 = fork(recolor_i, color, t628)
    except:
        t835 = None
    try:
        t836 = mapply(dneighbors, t54)
    except:
        t836 = None
    try:
        t837 = apply(t281, t630)
    except:
        t837 = None
    try:
        t838 = sizefilter(t631, ONE)
    except:
        t838 = None
    try:
        t839 = chain(even, t65, t633)
    except:
        t839 = None
    try:
        t840 = decrement(t185)
    except:
        t840 = None
    try:
        t841 = hconcat(t636, t453)
    except:
        t841 = None
    if t841 == O:
        return True, f'e9afcf9a - t841'
    try:
        t842 = color(t638)
    except:
        t842 = None
    try:
        t843 = other_f(t123, t251)
    except:
        t843 = None
    try:
        t844 = fill(I, t246, t640)
    except:
        t844 = None
    if t844 == O:
        return True, f'32597951 - t844'
    try:
        t845 = f_ofcolor(t641, BURGUNDY)
    except:
        t845 = None
    try:
        t846 = paint(I, t642)
    except:
        t846 = None
    try:
        t847 = subtract(t459, t644)
    except:
        t847 = None
    try:
        t848 = switch(t295, t462, t646)
    except:
        t848 = None
    if t848 == O:
        return True, f'b94a9452 - t848'
    try:
        t849 = f_ofcolor(I, t647)
    except:
        t849 = None
    try:
        t850 = corner(t648, R1)
    except:
        t850 = None
    try:
        t851 = astuple(UNITY, NEG_UNITY)
    except:
        t851 = None
    try:
        t852 = chain(outbox, outbox, initset)
    except:
        t852 = None
    try:
        t853 = compose(merge, t652)
    except:
        t853 = None
    try:
        t854 = lbind(position, t467)
    except:
        t854 = None
    try:
        t855 = paint(I, t655)
    except:
        t855 = None
    try:
        t856 = f_ofcolor(I, TWO)
    except:
        t856 = None
    try:
        t857 = corner(t657, R3)
    except:
        t857 = None
    try:
        t858 = hconcat(t658, t303)
    except:
        t858 = None
    try:
        t859 = subgrid(t659, I)
    except:
        t859 = None
    try:
        t860 = fork(connect, t100, t660)
    except:
        t860 = None
    try:
        t861 = paint(I, t661)
    except:
        t861 = None
    try:
        t862 = merge_f(t662)
    except:
        t862 = None
    try:
        t863 = compose(t474, t10)
    except:
        t863 = None
    try:
        t864 = fill(I, t246, t663)
    except:
        t864 = None
    if t864 == O:
        return True, f'c1d99e64 - t864'
    try:
        t865 = center(t106)
    except:
        t865 = None
    try:
        t866 = mir_rot_t(t664, R3)
    except:
        t866 = None
    if t866 == O:
        return True, f'3906de3d - t866'
    try:
        t867 = paint(t48, t666)
    except:
        t867 = None
    if t867 == O:
        return True, f'e3497940 - t867'
    try:
        t868 = vconcat(t149, t667)
    except:
        t868 = None
    if t868 == O:
        return True, f'46442a0e - t868'
    try:
        t869 = fill(t478, CYAN, t80)
    except:
        t869 = None
    if t869 == O:
        return True, f'd0f5fe59 - t869'
    try:
        t870 = increment(t668)
    except:
        t870 = None
    try:
        t871 = mapply(t14, t669)
    except:
        t871 = None
    try:
        t872 = apply(size, t670)
    except:
        t872 = None
    try:
        t873 = upscale_t(t482, t671)
    except:
        t873 = None
    try:
        t874 = compose(t672, palette_f)
    except:
        t874 = None
    try:
        t875 = corner(t318, R1)
    except:
        t875 = None
    try:
        t876 = subtract(t486, t674)
    except:
        t876 = None
    try:
        t877 = corner(t157, R1)
    except:
        t877 = None
    try:
        t878 = fill(I, t264, t678)
    except:
        t878 = None
    try:
        t879 = chain(positive, decrement, t680)
    except:
        t879 = None
    try:
        t880 = apply(toindices, t207)
    except:
        t880 = None
    try:
        t881 = divide(t681, THREE)
    except:
        t881 = None
    try:
        t882 = hconcat(t440, t266)
    except:
        t882 = None
    try:
        t883 = mapply(outbox, t682)
    except:
        t883 = None
    try:
        t884 = order(t323, t683)
    except:
        t884 = None
    try:
        t885 = fill(I, CYAN, t684)
    except:
        t885 = None
    try:
        t886 = lbind(t36, t125)
    except:
        t886 = None
    try:
        t887 = fill(I, t495, t685)
    except:
        t887 = None
    if t887 == O:
        return True, f'928ad970 - t887'
    try:
        t888 = difference(t20, t165)
    except:
        t888 = None
    try:
        t889 = lbind(mapply, neighbors)
    except:
        t889 = None
    try:
        t890 = rbind(divide, GREEN)
    except:
        t890 = None
    try:
        t891 = get_rank(t688, L1)
    except:
        t891 = None
    try:
        t892 = compose(t501, t689)
    except:
        t892 = None
    try:
        t893 = lbind(rbind, sfilter)
    except:
        t893 = None
    try:
        t894 = astuple(t692, t692)
    except:
        t894 = None
    try:
        t895 = compose(t693, dneighbors)
    except:
        t895 = None
    try:
        t896 = compose(t506, t694)
    except:
        t896 = None
    try:
        t897 = rbind(greater, BLUE)
    except:
        t897 = None
    try:
        t898 = gravitate(t333, t697)
    except:
        t898 = None
    try:
        t899 = dedupe(t698)
    except:
        t899 = None
    try:
        t900 = mapply(t510, t7)
    except:
        t900 = None
    try:
        t901 = branch(t699, ZERO_BY_TWO, TWO_BY_ZERO)
    except:
        t901 = None
    try:
        t902 = power(trim, TWO)
    except:
        t902 = None
    try:
        t903 = insert(FOUR, t701)
    except:
        t903 = None
    try:
        t904 = f_ofcolor(t86, BLACK)
    except:
        t904 = None
    if t844 == O:
        return True, f'6d75e8bb - t844'
    try:
        t905 = fork(add, t10, t23)
    except:
        t905 = None
    try:
        t906 = mpapply(recolor_o, t515, t703)
    except:
        t906 = None
    try:
        t907 = sizefilter(t704, ONE)
    except:
        t907 = None
    try:
        t908 = initset(I)
    except:
        t908 = None
    try:
        t909 = mfilter_f(t706, hline_o)
    except:
        t909 = None
    try:
        t910 = remove_f(t517, t176)
    except:
        t910 = None
    try:
        t911 = apply(t58, t710)
    except:
        t911 = None
    try:
        t912 = lbind(shift, t712)
    except:
        t912 = None
    try:
        t913 = compose(t521, t713)
    except:
        t913 = None
    try:
        t914 = apply(t714, t522)
    except:
        t914 = None
    try:
        t915 = t715(I)
    except:
        t915 = None
    try:
        t916 = compose(even, t716)
    except:
        t916 = None
    try:
        t917 = mapply(vfrontier, t91)
    except:
        t917 = None
    try:
        t918 = mapply(t718, t7)
    except:
        t918 = None
    try:
        t919 = lbind(subtract, t719)
    except:
        t919 = None
    try:
        t920 = replace(I, t251, t300)
    except:
        t920 = None
    try:
        t921 = fork(connect, t298, t721)
    except:
        t921 = None
    try:
        t922 = canvas(ZERO, t722)
    except:
        t922 = None
    try:
        t923 = colorfilter(t8, BURGUNDY)
    except:
        t923 = None
    try:
        t924 = recolor_i(t184, t723)
    except:
        t924 = None
    try:
        t925 = mir_rot_t(t724, R0)
    except:
        t925 = None
    try:
        t926 = remove_f(t186, t17)
    except:
        t926 = None
    try:
        t927 = astuple(t35, t439)
    except:
        t927 = None
    try:
        t928 = difference(t17, t725)
    except:
        t928 = None
    try:
        t929 = col_row(t187, R1)
    except:
        t929 = None
    try:
        t930 = equality(t728, YELLOW)
    except:
        t930 = None
    try:
        t931 = mapply(backdrop, t729)
    except:
        t931 = None
    try:
        t932 = lbind(mapply, t731)
    except:
        t932 = None
    try:
        t933 = sfilter_f(t207, square_f)
    except:
        t933 = None
    try:
        t934 = canvas(BLACK, t39)
    except:
        t934 = None
    if t868 == O:
        return True, f'7fe24cdd - t868'
    try:
        t935 = compose(flip, t733)
    except:
        t935 = None
    try:
        t936 = width_f(t6)
    except:
        t936 = None
    try:
        t937 = compose(t10, t735)
    except:
        t937 = None
    try:
        t938 = mpapply(recolor_o, t538, t736)
    except:
        t938 = None
    try:
        t939 = hupscale(t739, t74)
    except:
        t939 = None
    try:
        t940 = lbind(hupscale, t740)
    except:
        t940 = None
    try:
        t941 = lbind(astuple, t185)
    except:
        t941 = None
    try:
        t942 = apply(initset, t741)
    except:
        t942 = None
    try:
        t943 = branch(t544, identity, t18)
    except:
        t943 = None
    try:
        t944 = color(t187)
    except:
        t944 = None
    try:
        t945 = f_ofcolor(I, ONE)
    except:
        t945 = None
    try:
        t946 = crop(I, t203, t746)
    except:
        t946 = None
    try:
        t947 = get_arg_rank_f(t204, size, F0)
    except:
        t947 = None
    try:
        t948 = t749(I)
    except:
        t948 = None
    try:
        t949 = compose(crement, t750)
    except:
        t949 = None
    try:
        t950 = outbox(t752)
    except:
        t950 = None
    try:
        t951 = canvas(BLUE, t753)
    except:
        t951 = None
    try:
        t952 = lbind(compose, t754)
    except:
        t952 = None
    try:
        t953 = mapply(outbox, t755)
    except:
        t953 = None
    try:
        t954 = fork(apply, t21, t170)
    except:
        t954 = None
    try:
        t955 = toobject(t756, I)
    except:
        t955 = None
    try:
        t956 = merge_t(t757)
    except:
        t956 = None
    try:
        t957 = colorfilter(t8, t251)
    except:
        t957 = None
    try:
        t958 = compress(t760)
    except:
        t958 = None
    try:
        t959 = cover(I, t761)
    except:
        t959 = None
    try:
        t960 = mapply(outbox, t171)
    except:
        t960 = None
    try:
        t961 = prapply(connect, t563, t91)
    except:
        t961 = None
    try:
        t962 = interval(NEG_TWO, FOUR, ONE)
    except:
        t962 = None
    try:
        t963 = canvas(t251, t765)
    except:
        t963 = None
    try:
        t964 = subgrid(t766, I)
    except:
        t964 = None
    if t964 == O:
        return True, f'48d8fb45 - t964'
    try:
        t965 = mfilter_f(t767, square_f)
    except:
        t965 = None
    try:
        t966 = fill(I, t264, t768)
    except:
        t966 = None
    try:
        t967 = mapply(neighbors, t769)
    except:
        t967 = None
    try:
        t968 = compose(even, height_f)
    except:
        t968 = None
    try:
        t969 = subgrid(t427, t43)
    except:
        t969 = None
    try:
        t970 = difference(t172, t771)
    except:
        t970 = None
    try:
        t971 = decrement(t772)
    except:
        t971 = None
    try:
        t972 = get_nth_f(t774, F0)
    except:
        t972 = None
    try:
        t973 = branch(t570, t18, identity)
    except:
        t973 = None
    try:
        t974 = colorfilter(t8, GRAY)
    except:
        t974 = None
    try:
        t975 = fill(I, t246, t775)
    except:
        t975 = None
    if t975 == O:
        return True, f'60b61512 - t975'
    try:
        t976 = combine(t80, t776)
    except:
        t976 = None
    try:
        t977 = recolor_o(BLUE, t777)
    except:
        t977 = None
    try:
        t978 = apply(normalize, t778)
    except:
        t978 = None
    try:
        t979 = color(t779)
    except:
        t979 = None
    try:
        t980 = subgrid(t781, I)
    except:
        t980 = None
    try:
        t981 = compose(t302, t398)
    except:
        t981 = None
    try:
        t982 = width_t(t282)
    except:
        t982 = None
    try:
        t983 = fill(I, t246, t783)
    except:
        t983 = None
    try:
        t984 = apply(t579, t784)
    except:
        t984 = None
    try:
        t985 = colorfilter(t8, YELLOW)
    except:
        t985 = None
    try:
        t986 = normalize(t785)
    except:
        t986 = None
    try:
        t987 = combine(t404, t786)
    except:
        t987 = None
    try:
        t988 = paint(t405, t99)
    except:
        t988 = None
    try:
        t989 = fork(equality, toindices, backdrop)
    except:
        t989 = None
    try:
        t990 = mir_rot_t(t787, R0)
    except:
        t990 = None
    try:
        t991 = equality(t788, BLACK)
    except:
        t991 = None
    try:
        t992 = mir_rot_t(t789, R0)
    except:
        t992 = None
    if t992 == O:
        return True, f'8d5021e8 - t992'
    try:
        t993 = mir_rot_f(t790, R2)
    except:
        t993 = None
    try:
        t994 = normalize_o(t791)
    except:
        t994 = None
    try:
        t995 = replace(I, t251, t264)
    except:
        t995 = None
    try:
        t996 = interval(FOUR, t792, FOUR)
    except:
        t996 = None
    try:
        t997 = paint(t589, t793)
    except:
        t997 = None
    try:
        t998 = fork(recolor_i, t410, t795)
    except:
        t998 = None
    try:
        t999 = portrait_f(t333)
    except:
        t999 = None
    try:
        t1000 = shape_f(t412)
    except:
        t1000 = None
    try:
        t1001 = fill(I, t413, t797)
    except:
        t1001 = None
    try:
        t1002 = greater(t593, t798)
    except:
        t1002 = None
    try:
        t1003 = dneighbors(t799)
    except:
        t1003 = None
    try:
        t1004 = initset(t799)
    except:
        t1004 = None
    try:
        t1005 = fill(I, t246, t800)
    except:
        t1005 = None
    try:
        t1006 = astuple(FOUR, EIGHT)
    except:
        t1006 = None
    try:
        t1007 = fork(shift, identity, t803)
    except:
        t1007 = None
    try:
        t1008 = cover(I, t808)
    except:
        t1008 = None
    try:
        t1009 = f_ofcolor(I, t247)
    except:
        t1009 = None
    try:
        t1010 = o_g(t809, R7)
    except:
        t1010 = None
    try:
        t1011 = intersection(t605, t810)
    except:
        t1011 = None
    try:
        t1012 = interval(ZERO, NINE, ONE)
    except:
        t1012 = None
    try:
        t1013 = vconcat(I, I)
    except:
        t1013 = None
    try:
        t1014 = chain(flip, t672, palette_t)
    except:
        t1014 = None
    try:
        t1015 = vfrontier(t814)
    except:
        t1015 = None
    try:
        t1016 = rbind(contained, t815)
    except:
        t1016 = None
    try:
        t1017 = compose(t816, numcolors_t)
    except:
        t1017 = None
    try:
        t1018 = fork(connect, t100, t817)
    except:
        t1018 = None
    try:
        t1019 = chain(t612, t232, dneighbors)
    except:
        t1019 = None
    try:
        t1020 = color(t818)
    except:
        t1020 = None
    try:
        t1021 = f_ofcolor(t11, BLACK)
    except:
        t1021 = None
    try:
        t1022 = replace(t434, t251, BLACK)
    except:
        t1022 = None
    try:
        t1023 = fill(I, t246, t819)
    except:
        t1023 = None
    if t1023 == O:
        return True, f'50cb2852 - t1023'
    try:
        t1024 = astuple(NEG_TWO, NEG_TWO)
    except:
        t1024 = None
    try:
        t1025 = compose(t617, t823)
    except:
        t1025 = None
    try:
        t1026 = fill(I, t264, t824)
    except:
        t1026 = None
    try:
        t1027 = branch(t826, UP, RIGHT)
    except:
        t1027 = None
    try:
        t1028 = chain(outbox, outbox, t827)
    except:
        t1028 = None
    try:
        t1029 = merge_f(t828)
    except:
        t1029 = None
    try:
        t1030 = righthalf(t11)
    except:
        t1030 = None
    try:
        t1031 = shoot(t829, NEG_UNITY)
    except:
        t1031 = None
    try:
        t1032 = recolor_i(BLACK, t830)
    except:
        t1032 = None
    try:
        t1033 = fork(either, hline_i, vline_i)
    except:
        t1033 = None
    try:
        t1034 = rbind(contained, t833)
    except:
        t1034 = None
    try:
        t1035 = multiply(t277, THREE)
    except:
        t1035 = None
    try:
        t1036 = fill(t24, t246, t836)
    except:
        t1036 = None
    try:
        t1037 = sfilter_f(t629, t384)
    except:
        t1037 = None
    try:
        t1038 = merge_f(t838)
    except:
        t1038 = None
    try:
        t1039 = compose(even, t23)
    except:
        t1039 = None
    try:
        t1040 = astuple(t840, ONE)
    except:
        t1040 = None
    try:
        t1041 = t215(t452)
    except:
        t1041 = None
    try:
        t1042 = shift(t29, UP)
    except:
        t1042 = None
    try:
        t1043 = other_f(t123, t842)
    except:
        t1043 = None
    try:
        t1044 = power(t10, TWO)
    except:
        t1044 = None
    try:
        t1045 = lbind(colorfilter, t301)
    except:
        t1045 = None
    try:
        t1046 = fill(t457, BURGUNDY, t845)
    except:
        t1046 = None
    try:
        t1047 = increment(t847)
    except:
        t1047 = None
    try:
        t1048 = apply(t298, t729)
    except:
        t1048 = None
    try:
        t1049 = size_f(t849)
    except:
        t1049 = None
    try:
        t1050 = colorcount_t(I, t251)
    except:
        t1050 = None
    try:
        t1051 = shoot(t850, NEG_UNITY)
    except:
        t1051 = None
    try:
        t1052 = astuple(UP_RIGHT, DOWN_LEFT)
    except:
        t1052 = None
    try:
        t1053 = corners(t465)
    except:
        t1053 = None
    try:
        t1054 = mapply(t651, t7)
    except:
        t1054 = None
    try:
        t1055 = t853(TWO)
    except:
        t1055 = None
    try:
        t1056 = fork(shoot, center, t854)
    except:
        t1056 = None
    try:
        t1057 = t656(t856)
    except:
        t1057 = None
    try:
        t1058 = shoot(t857, UP_RIGHT)
    except:
        t1058 = None
    try:
        t1059 = vconcat(t858, t858)
    except:
        t1059 = None
    try:
        t1060 = asobject(t859)
    except:
        t1060 = None
    try:
        t1061 = chain(initset, center, t860)
    except:
        t1061 = None
    try:
        t1062 = subgrid(t862, I)
    except:
        t1062 = None
    try:
        t1063 = compose(t45, t863)
    except:
        t1063 = None
    try:
        t1064 = subtract(t865, t248)
    except:
        t1064 = None
    try:
        t1065 = fill(t665, BLACK, t181)
    except:
        t1065 = None
    if t1065 == O:
        return True, f'c9f8e694 - t1065'
    try:
        t1066 = branch(t479, t668, t870)
    except:
        t1066 = None
    try:
        t1067 = underfill(I, t264, t871)
    except:
        t1067 = None
    try:
        t1068 = merge_f(t397)
    except:
        t1068 = None
    try:
        t1069 = increment(t872)
    except:
        t1069 = None
    if t1065 == O:
        return True, f'c7d4e6ad - t1065'
    try:
        t1070 = sfilter_f(t12, t874)
    except:
        t1070 = None
    try:
        t1071 = shoot(t875, UP_RIGHT)
    except:
        t1071 = None
    try:
        t1072 = sign(t876)
    except:
        t1072 = None
    try:
        t1073 = f_ofcolor(t155, t2)
    except:
        t1073 = None
    try:
        t1074 = colorfilter(t7, GREEN)
    except:
        t1074 = None
    try:
        t1075 = replace(I, t2, GRAY)
    except:
        t1075 = None
    try:
        t1076 = branch(t676, t320, t877)
    except:
        t1076 = None
    try:
        t1077 = rbind(colorcount_t, t2)
    except:
        t1077 = None
    try:
        t1078 = rbind(toobject, t158)
    except:
        t1078 = None
    try:
        t1079 = lbind(extract, t880)
    except:
        t1079 = None
    try:
        t1080 = upscale_f(t157, t881)
    except:
        t1080 = None
    try:
        t1081 = vconcat(t882, t882)
    except:
        t1081 = None
    try:
        t1082 = fill(I, t246, t883)
    except:
        t1082 = None
    if t1082 == O:
        return True, f'b27ca6d3 - t1082'
    try:
        t1083 = apply(t58, t884)
    except:
        t1083 = None
    try:
        t1084 = lbind(rbind, manhattan)
    except:
        t1084 = None
    try:
        t1085 = f_ofcolor(t48, BLACK)
    except:
        t1085 = None
    try:
        t1086 = get_nth_f(t888, F0)
    except:
        t1086 = None
    try:
        t1087 = power(t889, TWO)
    except:
        t1087 = None
    try:
        t1088 = compose(t567, t890)
    except:
        t1088 = None
    try:
        t1089 = col_row(t53, R2)
    except:
        t1089 = None
    try:
        t1090 = chain(invert, halve, shape_f)
    except:
        t1090 = None
    try:
        t1091 = compose(t691, t893)
    except:
        t1091 = None
    try:
        t1092 = crop(I, ORIGIN, t894)
    except:
        t1092 = None
    try:
        t1093 = sfilter_f(t91, t895)
    except:
        t1093 = None
    try:
        t1094 = fork(sfilter, identity, t896)
    except:
        t1094 = None
    try:
        t1095 = compose(t897, size)
    except:
        t1095 = None
    try:
        t1096 = move(I, t333, t898)
    except:
        t1096 = None
    if t1096 == O:
        return True, f'05f2a901 - t1096'
    try:
        t1097 = mir_rot_t(t899, R6)
    except:
        t1097 = None
    if t1097 == O:
        return True, f'90c28cc7 - t1097'
    try:
        t1098 = paint(I, t900)
    except:
        t1098 = None
    try:
        t1099 = move(I, t131, t901)
    except:
        t1099 = None
    if t1099 == O:
        return True, f'5168d44c - t1099'
    try:
        t1100 = t902(t295)
    except:
        t1100 = None
    try:
        t1101 = lbind(occurrences, t700)
    except:
        t1101 = None
    try:
        t1102 = insert(EIGHT, t903)
    except:
        t1102 = None
    try:
        t1103 = rbind(difference, t181)
    except:
        t1103 = None
    try:
        t1104 = f_ofcolor(t86, BLUE)
    except:
        t1104 = None
    try:
        t1105 = mfilter_f(t8, t553)
    except:
        t1105 = None
    try:
        t1106 = paint(I, t906)
    except:
        t1106 = None
    if t1106 == O:
        return True, f'08ed6ac7 - t1106'
    try:
        t1107 = difference(t704, t907)
    except:
        t1107 = None
    try:
        t1108 = insert(t49, t908)
    except:
        t1108 = None
    try:
        t1109 = toindices(t909)
    except:
        t1109 = None
    try:
        t1110 = combine_t(t707, t910)
    except:
        t1110 = None
    try:
        t1111 = chain(t518, t708, t694)
    except:
        t1111 = None
    try:
        t1112 = merge_t(t911)
    except:
        t1112 = None
    try:
        t1113 = papply(equality, t522, t914)
    except:
        t1113 = None
    try:
        t1114 = astuple(ONE, t915)
    except:
        t1114 = None
    try:
        t1115 = lbind(compose, t916)
    except:
        t1115 = None
    try:
        t1116 = underfill(I, t246, t917)
    except:
        t1116 = None
    try:
        t1117 = paint(t347, t918)
    except:
        t1117 = None
    if t1117 == O:
        return True, f'5521c0d9 - t1117'
    try:
        t1118 = lbind(power, outbox)
    except:
        t1118 = None
    try:
        t1119 = t921(t181)
    except:
        t1119 = None
    try:
        t1120 = hconcat(I, t922)
    except:
        t1120 = None
    try:
        t1121 = o_g(t261, R1)
    except:
        t1121 = None
    try:
        t1122 = lbind(shift, t924)
    except:
        t1122 = None
    try:
        t1123 = vconcat(I, t925)
    except:
        t1123 = None
    try:
        t1124 = apply(t298, t926)
    except:
        t1124 = None
    try:
        t1125 = tojvec(FOUR)
    except:
        t1125 = None
    try:
        t1126 = get_nth_f(t928, F0)
    except:
        t1126 = None
    try:
        t1127 = increment(t929)
    except:
        t1127 = None
    try:
        t1128 = compose(t18, dedupe)
    except:
        t1128 = None
    try:
        t1129 = branch(t930, NEG_ONE, BLUE)
    except:
        t1129 = None
    try:
        t1130 = fill(I, t246, t931)
    except:
        t1130 = None
    if t1130 == O:
        return True, f'ce22a75a - t1130'
    try:
        t1131 = chain(double, decrement, width_f)
    except:
        t1131 = None
    try:
        t1132 = fill(I, BLACK, t427)
    except:
        t1132 = None
    try:
        t1133 = merge_f(t933)
    except:
        t1133 = None
    try:
        t1134 = astuple(THREE, ORIGIN)
    except:
        t1134 = None
    try:
        t1135 = paint(t732, t62)
    except:
        t1135 = None
    try:
        t1136 = sfilter_f(t26, t935)
    except:
        t1136 = None
    try:
        t1137 = tojvec(t936)
    except:
        t1137 = None
    try:
        t1138 = fill(I, t300, t288)
    except:
        t1138 = None
    try:
        t1139 = paint(I, t938)
    except:
        t1139 = None
    if t1139 == O:
        return True, f'85c4e7cd - t1139'
    try:
        t1140 = bottomhalf(t148)
    except:
        t1140 = None
    try:
        t1141 = repeat(t939, RED)
    except:
        t1141 = None
    try:
        t1142 = chain(t940, decrement, height_t)
    except:
        t1142 = None
    try:
        t1143 = lbind(t193, t942)
    except:
        t1143 = None
    try:
        t1144 = mapply(t742, t7)
    except:
        t1144 = None
    try:
        t1145 = t943(I)
    except:
        t1145 = None
    try:
        t1146 = replace(t743, t944, t545)
    except:
        t1146 = None
    try:
        t1147 = lbind(matcher, t537)
    except:
        t1147 = None
    try:
        t1148 = subgrid(t945, I)
    except:
        t1148 = None
    try:
        t1149 = mir_rot_t(t946, R4)
    except:
        t1149 = None
    try:
        t1150 = normalize(t947)
    except:
        t1150 = None
    try:
        t1151 = size_f(t427)
    except:
        t1151 = None
    try:
        t1152 = fill(t748, GRAY, t54)
    except:
        t1152 = None
    if t1152 == O:
        return True, f'09629e4f - t1152'
    try:
        t1153 = o_g(t948, R5)
    except:
        t1153 = None
    try:
        t1154 = fork(shift, identity, t949)
    except:
        t1154 = None
    try:
        t1155 = subgrid(t950, I)
    except:
        t1155 = None
    try:
        t1156 = subtract(FIVE, t554)
    except:
        t1156 = None
    try:
        t1157 = chain(t55, t377, t952)
    except:
        t1157 = None
    try:
        t1158 = fill(I, t246, t953)
    except:
        t1158 = None
    try:
        t1159 = lbind(canvas, BLACK)
    except:
        t1159 = None
    try:
        t1160 = get_color_rank_f(t955, F0)
    except:
        t1160 = None
    try:
        t1161 = mir_rot_t(t956, R0)
    except:
        t1161 = None
    if t1161 == O:
        return True, f'f8ff0b80 - t1161'
    try:
        t1162 = sfilter_f(t957, square_f)
    except:
        t1162 = None
    try:
        t1163 = cellwise(t211, t441, ZERO)
    except:
        t1163 = None
    if t1163 == O:
        return True, f'007bbfb7 - t1163'
    try:
        t1164 = mir_rot_t(t437, R1)
    except:
        t1164 = None
    try:
        t1165 = mfilter_f(t759, t375)
    except:
        t1165 = None
    try:
        t1166 = fill(I, t246, t960)
    except:
        t1166 = None
    if t1166 == O:
        return True, f'dc1df850 - t1166'
    try:
        t1167 = apply(t764, t962)
    except:
        t1167 = None
    try:
        t1168 = vconcat(I, t963)
    except:
        t1168 = None
    try:
        t1169 = fill(I, t246, t965)
    except:
        t1169 = None
    if t1169 == O:
        return True, f'3aa6fb7a - t1169'
    try:
        t1170 = apply(t567, t967)
    except:
        t1170 = None
    try:
        t1171 = sfilter_f(t770, t968)
    except:
        t1171 = None
    try:
        t1172 = palette_t(t969)
    except:
        t1172 = None
    try:
        t1173 = normalize(t970)
    except:
        t1173 = None
    try:
        t1174 = t973(I)
    except:
        t1174 = None
    try:
        t1175 = mapply(t435, t974)
    except:
        t1175 = None
    try:
        t1176 = fill(I, BLACK, t976)
    except:
        t1176 = None
    if t1176 == O:
        return True, f'ea786f4a - t1176'
    try:
        t1177 = paint(I, t977)
    except:
        t1177 = None
    if t1177 == O:
        return True, f'9edfc990 - t1177'
    try:
        t1178 = chain(t394, t10, t823)
    except:
        t1178 = None
    try:
        t1179 = size(t978)
    except:
        t1179 = None
    try:
        t1180 = canvas(t979, UNITY)
    except:
        t1180 = None
    if t1180 == O:
        return True, f'b9b7f026 - t1180'
    try:
        t1181 = mapply(t780, t7)
    except:
        t1181 = None
    try:
        t1182 = color(t781)
    except:
        t1182 = None
    try:
        t1183 = fork(equality, t981, t302)
    except:
        t1183 = None
    try:
        t1184 = width_t(t399)
    except:
        t1184 = None
    try:
        t1185 = subgrid(t29, t983)
    except:
        t1185 = None
    try:
        t1186 = astuple(TWO, SIX)
    except:
        t1186 = None
    try:
        t1187 = get_arg_rank_f(t985, size, L1)
    except:
        t1187 = None
    try:
        t1188 = mapply(t93, t7)
    except:
        t1188 = None
    try:
        t1189 = lbind(shift, t986)
    except:
        t1189 = None
    try:
        t1190 = fill(t11, t226, t987)
    except:
        t1190 = None
    try:
        t1191 = portrait_f(t99)
    except:
        t1191 = None
    try:
        t1192 = sfilter_f(t207, t989)
    except:
        t1192 = None
    try:
        t1193 = vconcat(t787, t990)
    except:
        t1193 = None
    if t1193 == O:
        return True, f'496994bd - t1193'
    try:
        t1194 = lbind(shift, t993)
    except:
        t1194 = None
    try:
        t1195 = replace(t230, YELLOW, BLACK)
    except:
        t1195 = None
    try:
        t1196 = rbind(apply, t996)
    except:
        t1196 = None
    try:
        t1197 = get_arg_rank_f(t7, t302, L1)
    except:
        t1197 = None
    try:
        t1198 = mir_rot_f(t180, R1)
    except:
        t1198 = None
    try:
        t1199 = f_ofcolor(t409, t794)
    except:
        t1199 = None
    try:
        t1200 = matcher(t411, t251)
    except:
        t1200 = None
    try:
        t1201 = branch(t999, hsplit, vsplit)
    except:
        t1201 = None
    try:
        t1202 = add(t1000, TWO_BY_ZERO)
    except:
        t1202 = None
    try:
        t1203 = branch(t1002, hconcat, vconcat)
    except:
        t1203 = None
    try:
        t1204 = toobject(t1003, I)
    except:
        t1204 = None
    try:
        t1205 = fill(t238, t2, t1004)
    except:
        t1205 = None
    try:
        t1206 = remove(ZERO, t31)
    except:
        t1206 = None
    try:
        t1207 = replace(t437, t247, BLACK)
    except:
        t1207 = None
    try:
        t1208 = box(t54)
    except:
        t1208 = None
    try:
        t1209 = apply(tojvec, t1006)
    except:
        t1209 = None
    if t1169 == O:
        return True, f'44d8ac46 - t1169'
    try:
        t1210 = rbind(corner, R1)
    except:
        t1210 = None
    try:
        t1211 = normalize_o(t419)
    except:
        t1211 = None
    try:
        t1212 = subgrid(t126, t242)
    except:
        t1212 = None
    try:
        t1213 = sfilter_f(t207, t553)
    except:
        t1213 = None
    try:
        t1214 = f_ofcolor(t48, t247)
    except:
        t1214 = None
    try:
        t1215 = interval(ZERO, t47, ONE)
    except:
        t1215 = None
    try:
        t1216 = color(t808)
    except:
        t1216 = None
    try:
        t1217 = lbind(sfilter, t1009)
    except:
        t1217 = None
    try:
        t1218 = get_nth_f(t1010, F0)
    except:
        t1218 = None
    try:
        t1219 = fill(I, t246, t1011)
    except:
        t1219 = None
    if t1219 == O:
        return True, f'a699fb00 - t1219'
    try:
        t1220 = apply(t811, t1012)
    except:
        t1220 = None
    try:
        t1221 = branch(t92, t246, t264)
    except:
        t1221 = None
    try:
        t1222 = vconcat(t1013, I)
    except:
        t1222 = None
    try:
        t1223 = mfilter_f(t8, t1014)
    except:
        t1223 = None
    try:
        t1224 = fill(t428, CYAN, t1015)
    except:
        t1224 = None
    try:
        t1225 = sfilter_t(t610, t1017)
    except:
        t1225 = None
    try:
        t1226 = rbind(sfilter, t1019)
    except:
        t1226 = None
    try:
        t1227 = colorfilter(t7, t1020)
    except:
        t1227 = None
    try:
        t1228 = compress(t1022)
    except:
        t1228 = None
    try:
        t1229 = rbind(mir_rot_t, R4)
    except:
        t1229 = None
    try:
        t1230 = sfilter_f(t7, square_f)
    except:
        t1230 = None
    try:
        t1231 = shift(t822, t1024)
    except:
        t1231 = None
    try:
        t1232 = apply(color, t7)
    except:
        t1232 = None
    try:
        t1233 = center(t108)
    except:
        t1233 = None
    try:
        t1234 = colorfilter(t8, t2)
    except:
        t1234 = None
    try:
        t1235 = subgrid(t1029, I)
    except:
        t1235 = None
    try:
        t1236 = f_ofcolor(t1030, YELLOW)
    except:
        t1236 = None
    try:
        t1237 = fill(t445, BLUE, t1031)
    except:
        t1237 = None
    if t1237 == O:
        return True, f'5c0a986e - t1237'
    try:
        t1238 = occurrences(I, t1032)
    except:
        t1238 = None
    try:
        t1239 = box(t112)
    except:
        t1239 = None
    try:
        t1240 = tojvec(t1035)
    except:
        t1240 = None
    try:
        t1241 = mapply(t835, t20)
    except:
        t1241 = None
    try:
        t1242 = mapply(ineighbors, t54)
    except:
        t1242 = None
    try:
        t1243 = dneighbors(UNITY)
    except:
        t1243 = None
    try:
        t1244 = difference(t629, t1037)
    except:
        t1244 = None
    try:
        t1245 = mfilter_f(t837, t384)
    except:
        t1245 = None
    try:
        t1246 = fill(I, t246, t1038)
    except:
        t1246 = None
    if t1246 == O:
        return True, f'aedd82e4 - t1246'
    try:
        t1247 = sfilter_f(t634, t1039)
    except:
        t1247 = None
    try:
        t1248 = mfilter_f(t207, t553)
    except:
        t1248 = None
    try:
        t1249 = product(t29, t29)
    except:
        t1249 = None
    try:
        t1250 = shoot(t1040, UP_RIGHT)
    except:
        t1250 = None
    try:
        t1251 = rbind(intersection, t1041)
    except:
        t1251 = None
    try:
        t1252 = fill(t285, t246, t1042)
    except:
        t1252 = None
    try:
        t1253 = corner(t638, R3)
    except:
        t1253 = None
    try:
        t1254 = rbind(shoot, NEG_UNITY)
    except:
        t1254 = None
    try:
        t1255 = chain(t10, t1045, color)
    except:
        t1255 = None
    try:
        t1256 = f_ofcolor(t127, YELLOW)
    except:
        t1256 = None
    try:
        t1257 = move(I, t131, t1047)
    except:
        t1257 = None
    if t1257 == O:
        return True, f'a1570a43 - t1257'
    try:
        t1258 = order(t9, t302)
    except:
        t1258 = None
    try:
        t1259 = apply(t298, t9)
    except:
        t1259 = None
    try:
        t1260 = fill(I, t246, t1048)
    except:
        t1260 = None
    try:
        t1261 = astuple(ONE, t1049)
    except:
        t1261 = None
    try:
        t1262 = positive(t1050)
    except:
        t1262 = None
    try:
        t1263 = fill(t463, BLUE, t1051)
    except:
        t1263 = None
    try:
        t1264 = combine(t851, t1052)
    except:
        t1264 = None
    try:
        t1265 = mapply(t852, t1053)
    except:
        t1265 = None
    try:
        t1266 = paint(t137, t1054)
    except:
        t1266 = None
    if t1266 == O:
        return True, f'd13f3404 - t1266'
    try:
        t1267 = fill(I, t300, t1055)
    except:
        t1267 = None
    try:
        t1268 = backdrop(t106)
    except:
        t1268 = None
    try:
        t1269 = mapply(t1056, t125)
    except:
        t1269 = None
    try:
        t1270 = o_g(t48, R5)
    except:
        t1270 = None
    try:
        t1271 = t656(t42)
    except:
        t1271 = None
    try:
        t1272 = shoot(t857, NEG_UNITY)
    except:
        t1272 = None
    try:
        t1273 = vconcat(t1059, t858)
    except:
        t1273 = None
    try:
        t1274 = fork(recolor_i, t143, t1061)
    except:
        t1274 = None
    try:
        t1275 = index(t1062, DOWN)
    except:
        t1275 = None
    try:
        t1276 = fork(shoot, identity, t1063)
    except:
        t1276 = None
    try:
        t1277 = shoot(t248, t1064)
    except:
        t1277 = None
    try:
        t1278 = product(t125, t142)
    except:
        t1278 = None
    try:
        t1279 = compose(t23, center)
    except:
        t1279 = None
    try:
        t1280 = double(t1066)
    except:
        t1280 = None
    try:
        t1281 = delta(t1068)
    except:
        t1281 = None
    try:
        t1282 = canvas(t50, t1069)
    except:
        t1282 = None
    if t1282 == O:
        return True, f'1190e5a7 - t1282'
    try:
        t1283 = rbind(repeat, t671)
    except:
        t1283 = None
    try:
        t1284 = size_f(t1070)
    except:
        t1284 = None
    try:
        t1285 = combine(t673, t1071)
    except:
        t1285 = None
    try:
        t1286 = move(I, t154, t1072)
    except:
        t1286 = None
    if t1286 == O:
        return True, f'dc433765 - t1286'
    try:
        t1287 = mapply(ineighbors, t1073)
    except:
        t1287 = None
    try:
        t1288 = get_nth_f(t1074, F0)
    except:
        t1288 = None
    try:
        t1289 = t488(t1075)
    except:
        t1289 = None
    try:
        t1290 = branch(t676, UNITY, DOWN_LEFT)
    except:
        t1290 = None
    try:
        t1291 = get_arg_rank_f(t677, t1077, F0)
    except:
        t1291 = None
    try:
        t1292 = chain(t879, t1078, dneighbors)
    except:
        t1292 = None
    try:
        t1293 = lbind(lbind, contained)
    except:
        t1293 = None
    try:
        t1294 = normalize(t1080)
    except:
        t1294 = None
    try:
        t1295 = double(t150)
    except:
        t1295 = None
    try:
        t1296 = vconcat(t1081, t882)
    except:
        t1296 = None
    try:
        t1297 = merge_t(t1083)
    except:
        t1297 = None
    try:
        t1298 = canvas(CYAN, t28)
    except:
        t1298 = None
    try:
        t1299 = chain(t886, t1084, initset)
    except:
        t1299 = None
    try:
        t1300 = color(t1086)
    except:
        t1300 = None
    try:
        t1301 = fork(equality, identity, t1088)
    except:
        t1301 = None
    try:
        t1302 = astuple(t891, t1089)
    except:
        t1302 = None
    try:
        t1303 = shift(t6, NEG_UNITY)
    except:
        t1303 = None
    try:
        t1304 = fork(shift, t892, t1090)
    except:
        t1304 = None
    try:
        t1305 = compose(t331, size)
    except:
        t1305 = None
    try:
        t1306 = lbind(contained, TWO)
    except:
        t1306 = None
    try:
        t1307 = partition(t1092)
    except:
        t1307 = None
    try:
        t1308 = fill(I, BLACK, t1093)
    except:
        t1308 = None
    if t1308 == O:
        return True, f'7f4411dc - t1308'
    try:
        t1309 = fork(difference, identity, t1094)
    except:
        t1309 = None
    try:
        t1310 = sfilter_f(t695, t1095)
    except:
        t1310 = None
    try:
        t1311 = vsplit(t1098, THREE)
    except:
        t1311 = None
    try:
        t1312 = asindices(t1100)
    except:
        t1312 = None
    try:
        t1313 = get_nth_t(t512, L1)
    except:
        t1313 = None
    try:
        t1314 = product(t1102, t1102)
    except:
        t1314 = None
    try:
        t1315 = chain(size, t1103, t702)
    except:
        t1315 = None
    try:
        t1316 = combine_f(t904, t1104)
    except:
        t1316 = None
    try:
        t1317 = fill(I, t246, t1105)
    except:
        t1317 = None
    try:
        t1318 = t905(t29)
    except:
        t1318 = None
    try:
        t1319 = merge_f(t1107)
    except:
        t1319 = None
    try:
        t1320 = insert(t27, t1108)
    except:
        t1320 = None
    try:
        t1321 = fill(I, t264, t1109)
    except:
        t1321 = None
    try:
        t1322 = mpapply(recolor_o, t339, t1110)
    except:
        t1322 = None
    try:
        t1323 = fork(sfilter, identity, t1111)
    except:
        t1323 = None
    try:
        t1324 = rbind(vmatching, t53)
    except:
        t1324 = None
    try:
        t1325 = mir_rot_t(t1112, R1)
    except:
        t1325 = None
    try:
        t1326 = paint(t711, t98)
    except:
        t1326 = None
    if t1326 == O:
        return True, f'9565186b - t1326'
    try:
        t1327 = compose(toivec, numcolors_f)
    except:
        t1327 = None
    try:
        t1328 = difference(t7, t171)
    except:
        t1328 = None
    try:
        t1329 = pair(t522, t1113)
    except:
        t1329 = None
    try:
        t1330 = crop(t523, ORIGIN, t1114)
    except:
        t1330 = None
    try:
        t1331 = lbind(rbind, astuple)
    except:
        t1331 = None
    try:
        t1332 = hconcat(t1116, t1116)
    except:
        t1332 = None
    try:
        t1333 = recolor_o(t246, t126)
    except:
        t1333 = None
    try:
        t1334 = chain(toivec, t919, t586)
    except:
        t1334 = None
    try:
        t1335 = compose(width_f, inbox)
    except:
        t1335 = None
    try:
        t1336 = intersection(t181, t1119)
    except:
        t1336 = None
    try:
        t1337 = o_g(t1120, R7)
    except:
        t1337 = None
    try:
        t1338 = get_arg_rank_f(t1121, size, L1)
    except:
        t1338 = None
    try:
        t1339 = compose(decrement, double)
    except:
        t1339 = None
    try:
        t1340 = double(t185)
    except:
        t1340 = None
    try:
        t1341 = replace(t351, t251, t246)
    except:
        t1341 = None
    if t1341 == O:
        return True, f'c8f0f002 - t1341'
    try:
        t1342 = mapply(t530, t1124)
    except:
        t1342 = None
    try:
        t1343 = crop(I, t1125, THREE_BY_THREE)
    except:
        t1343 = None
    try:
        t1344 = normalize(t1126)
    except:
        t1344 = None
    try:
        t1345 = rbind(greater, t1127)
    except:
        t1345 = None
    try:
        t1346 = t1128(I)
    except:
        t1346 = None
    try:
        t1347 = multiply(t1129, THREE)
    except:
        t1347 = None
    try:
        t1348 = fgpartition(t523)
    except:
        t1348 = None
    try:
        t1349 = get_color_rank_t(t1132, L1)
    except:
        t1349 = None
    try:
        t1350 = fill(I, t264, t1133)
    except:
        t1350 = None
    try:
        t1351 = initset(t1134)
    except:
        t1351 = None
    try:
        t1352 = o_g(t1135, R1)
    except:
        t1352 = None
    try:
        t1353 = fill(I, BLACK, t1136)
    except:
        t1353 = None
    if t1353 == O:
        return True, f'd23f8c26 - t1353'
    try:
        t1354 = cover(I, t1126)
    except:
        t1354 = None
    try:
        t1355 = add(t1137, ZERO_BY_TWO)
    except:
        t1355 = None
    try:
        t1356 = t738(t1140)
    except:
        t1356 = None
    try:
        t1357 = merge_t(t1141)
    except:
        t1357 = None
    try:
        t1358 = compose(t543, t1142)
    except:
        t1358 = None
    try:
        t1359 = lbind(lbind, manhattan)
    except:
        t1359 = None
    try:
        t1360 = fill(I, t246, t1144)
    except:
        t1360 = None
    try:
        t1361 = lbind(mapply, vfrontier)
    except:
        t1361 = None
    try:
        t1362 = height_t(t1146)
    except:
        t1362 = None
    try:
        t1363 = mir_rot_t(t1148, R4)
    except:
        t1363 = None
    if t1341 == O:
        return True, f'a740d043 - t1341'
    try:
        t1364 = paint(t747, t1150)
    except:
        t1364 = None
    try:
        t1365 = equality(t1151, YELLOW)
    except:
        t1365 = None
    try:
        t1366 = mapply(t1154, t125)
    except:
        t1366 = None
    try:
        t1367 = fgpartition(t1155)
    except:
        t1367 = None
    try:
        t1368 = astuple(ONE, t1156)
    except:
        t1368 = None
    try:
        t1369 = chain(t954, asobject, t1159)
    except:
        t1369 = None
    try:
        t1370 = merge_f(t1162)
    except:
        t1370 = None
    try:
        t1371 = color(t126)
    except:
        t1371 = None
    try:
        t1372 = papply(pair, t437, t1164)
    except:
        t1372 = None
    try:
        t1373 = fill(I, t246, t1165)
    except:
        t1373 = None
    if t1373 == O:
        return True, f'6f8cd79b - t1373'
    try:
        t1374 = mfilter_f(t961, t384)
    except:
        t1374 = None
    try:
        t1375 = apply(toivec, t1167)
    except:
        t1375 = None
    try:
        t1376 = o_g(t1168, R1)
    except:
        t1376 = None
    try:
        t1377 = mapply(t388, t1170)
    except:
        t1377 = None
    try:
        t1378 = merge_f(t1171)
    except:
        t1378 = None
    try:
        t1379 = contained(t251, t1172)
    except:
        t1379 = None
    try:
        t1380 = matcher(t215, t1173)
    except:
        t1380 = None
    try:
        t1381 = height_f(t73)
    except:
        t1381 = None
    try:
        t1382 = fork(manhattan, t10, t23)
    except:
        t1382 = None
    try:
        t1383 = get_color_rank_f(t390, F0)
    except:
        t1383 = None
    try:
        t1384 = get_nth_f(t73, F0)
    except:
        t1384 = None
    try:
        t1385 = o_g(t1174, R4)
    except:
        t1385 = None
    try:
        t1386 = fill(I, t246, t1175)
    except:
        t1386 = None
    if t1386 == O:
        return True, f'bb43febb - t1386'
    try:
        t1387 = t1178(TWO)
    except:
        t1387 = None
    try:
        t1388 = interval(ZERO, t1179, ONE)
    except:
        t1388 = None
    try:
        t1389 = paint(I, t1181)
    except:
        t1389 = None
    try:
        t1390 = replace(t980, t1182, t2)
    except:
        t1390 = None
    if t1390 == O:
        return True, f'fcb5c309 - t1390'
    try:
        t1391 = compose(invert, t1183)
    except:
        t1391 = None
    try:
        t1392 = divide(t982, t1184)
    except:
        t1392 = None
    try:
        t1393 = f_ofcolor(t1185, BLUE)
    except:
        t1393 = None
    try:
        t1394 = astuple(FIVE, ONE)
    except:
        t1394 = None
    try:
        t1395 = get_arg_rank_f(t66, size, F0)
    except:
        t1395 = None
    try:
        t1396 = t435(t1187)
    except:
        t1396 = None
    try:
        t1397 = underfill(I, t246, t1188)
    except:
        t1397 = None
    if t1397 == O:
        return True, f'41e4d17e - t1397'
    try:
        t1398 = replace(t403, t251, t246)
    except:
        t1398 = None
    if t1398 == O:
        return True, f'a79310a0 - t1398'
    try:
        t1399 = mir_rot_t(t1190, R0)
    except:
        t1399 = None
    try:
        t1400 = matcher(size, BLACK)
    except:
        t1400 = None
    try:
        t1401 = branch(t991, identity, t714)
    except:
        t1401 = None
    try:
        t1402 = o_g(t1195, R5)
    except:
        t1402 = None
    try:
        t1403 = lbind(rbind, multiply)
    except:
        t1403 = None
    try:
        t1404 = col_row(t1197, R2)
    except:
        t1404 = None
    try:
        t1405 = paint(t997, t1198)
    except:
        t1405 = None
    try:
        t1406 = mapply(t299, t1199)
    except:
        t1406 = None
    try:
        t1407 = compose(double, t1200)
    except:
        t1407 = None
    try:
        t1408 = crop(I, t796, t1202)
    except:
        t1408 = None
    if t1408 == O:
        return True, f'3f7978a0 - t1408'
    try:
        t1409 = branch(t1002, lefthalf, tophalf)
    except:
        t1409 = None
    try:
        t1410 = get_color_rank_f(t1204, F0)
    except:
        t1410 = None
    try:
        t1411 = neighbors(t799)
    except:
        t1411 = None
    try:
        t1412 = lbind(colorcount_t, I)
    except:
        t1412 = None
    try:
        t1413 = compress(t1207)
    except:
        t1413 = None
    try:
        t1414 = difference(t1208, t54)
    except:
        t1414 = None
    try:
        t1415 = mpapply(shift, t801, t1209)
    except:
        t1415 = None
    try:
        t1416 = o_g(t802, R1)
    except:
        t1416 = None
    try:
        t1417 = mapply(t1007, t12)
    except:
        t1417 = None
    try:
        t1418 = lbind(lbind, colorcount_f)
    except:
        t1418 = None
    try:
        t1419 = lbind(t193, t1211)
    except:
        t1419 = None
    try:
        t1420 = mir_rot_t(t1212, R0)
    except:
        t1420 = None
    try:
        t1421 = mapply(t806, t123)
    except:
        t1421 = None
    try:
        t1422 = get_nth_f(t1213, F0)
    except:
        t1422 = None
    try:
        t1423 = rbind(colorcount_t, BLACK)
    except:
        t1423 = None
    try:
        t1424 = rbind(greater, GREEN)
    except:
        t1424 = None
    try:
        t1425 = vline_o(t1218)
    except:
        t1425 = None
    try:
        t1426 = multiply(NEG_ONE, NINE)
    except:
        t1426 = None
    try:
        t1427 = canvas(t1221, UNITY)
    except:
        t1427 = None
    if t1427 == O:
        return True, f'44f52bb0 - t1427'
    try:
        t1428 = f_ofcolor(t1222, BLACK)
    except:
        t1428 = None
    try:
        t1429 = lbind(shift, t1223)
    except:
        t1429 = None
    try:
        t1430 = compose(t1016, t23)
    except:
        t1430 = None
    try:
        t1431 = merge(t1225)
    except:
        t1431 = None
    try:
        t1432 = chain(t10, t1226, toindices)
    except:
        t1432 = None
    try:
        t1433 = f_ofcolor(t5, BLACK)
    except:
        t1433 = None
    try:
        t1434 = fork(equality, identity, t1229)
    except:
        t1434 = None
    try:
        t1435 = difference(t7, t1230)
    except:
        t1435 = None
    try:
        t1436 = underpaint(I, t1231)
    except:
        t1436 = None
    try:
        t1437 = mapply(t1025, t1232)
    except:
        t1437 = None
    try:
        t1438 = asindices(t86)
    except:
        t1438 = None
    try:
        t1439 = add(t1027, t1233)
    except:
        t1439 = None
    try:
        t1440 = get_arg_rank_f(t1234, size, F0)
    except:
        t1440 = None
    try:
        t1441 = height_t(t1235)
    except:
        t1441 = None
    try:
        t1442 = fill(t623, YELLOW, t1236)
    except:
        t1442 = None
    try:
        t1443 = mapply(t624, t1238)
    except:
        t1443 = None
    try:
        t1444 = lbind(t193, t625)
    except:
        t1444 = None
    try:
        t1445 = rbind(difference, t1239)
    except:
        t1445 = None
    try:
        t1446 = compose(t1034, t10)
    except:
        t1446 = None
    try:
        t1447 = shift(t114, t1240)
    except:
        t1447 = None
    try:
        t1448 = paint(I, t1241)
    except:
        t1448 = None
    if t1448 == O:
        return True, f'1f876c06 - t1448'
    try:
        t1449 = fill(t1036, GRAY, t1242)
    except:
        t1449 = None
    if t1449 == O:
        return True, f'b60334d2 - t1449'
    try:
        t1450 = insert(UNITY, t1243)
    except:
        t1450 = None
    try:
        t1451 = fork(equality, identity, box)
    except:
        t1451 = None
    try:
        t1452 = underfill(I, CYAN, t1245)
    except:
        t1452 = None
    if t1452 == O:
        return True, f'ded97339 - t1452'
    try:
        t1453 = fill(t3, t246, t1247)
    except:
        t1453 = None
    try:
        t1454 = fill(I, t246, t1248)
    except:
        t1454 = None
    if t1454 == O:
        return True, f'a5313dff - t1454'
    try:
        t1455 = lbind(recolor_o, BLACK)
    except:
        t1455 = None
    try:
        t1456 = apply(t281, t1249)
    except:
        t1456 = None
    try:
        t1457 = fill(I, t246, t1250)
    except:
        t1457 = None
    try:
        t1458 = shoot(t1253, UNITY)
    except:
        t1458 = None
    try:
        t1459 = fork(combine, t299, t1254)
    except:
        t1459 = None
    try:
        t1460 = fork(gravitate, identity, t1255)
    except:
        t1460 = None
    try:
        t1461 = fill(t1046, YELLOW, t1256)
    except:
        t1461 = None
    if t1461 == O:
        return True, f'cf98881b - t1461'
    try:
        t1462 = mapply(t458, t427)
    except:
        t1462 = None
    try:
        t1463 = get_nth_t(t1258, F0)
    except:
        t1463 = None
    try:
        t1464 = mapply(t645, t1259)
    except:
        t1464 = None
    try:
        t1465 = canvas(t647, t1261)
    except:
        t1465 = None
    if t1465 == O:
        return True, f'd631b094 - t1465'
    try:
        t1466 = f_ofcolor(t1263, BLUE)
    except:
        t1466 = None
    try:
        t1467 = mapply(t649, t1264)
    except:
        t1467 = None
    try:
        t1468 = difference(t650, t1265)
    except:
        t1468 = None
    try:
        t1469 = compose(t170, t1094)
    except:
        t1469 = None
    try:
        t1470 = fill(I, t653, t1268)
    except:
        t1470 = None
    try:
        t1471 = fill(I, t654, t1269)
    except:
        t1471 = None
    if t1471 == O:
        return True, f'7ddcd7ec - t1471'
    try:
        t1472 = mapply(t139, t1270)
    except:
        t1472 = None
    try:
        t1473 = greater(t1057, t1271)
    except:
        t1473 = None
    try:
        t1474 = combine(t1058, t1272)
    except:
        t1474 = None
    try:
        t1475 = cellwise(t471, t1273, ZERO)
    except:
        t1475 = None
    if t1475 == O:
        return True, f'8f2ea7aa - t1475'
    try:
        t1476 = matcher(t10, BLACK)
    except:
        t1476 = None
    try:
        t1477 = subgrid(t473, I)
    except:
        t1477 = None
    try:
        t1478 = lbind(matcher, t863)
    except:
        t1478 = None
    try:
        t1479 = underfill(I, t2, t1277)
    except:
        t1479 = None
    if t1479 == O:
        return True, f'25d487eb - t1479'
    try:
        t1480 = fork(vmatching, t10, t23)
    except:
        t1480 = None
    try:
        t1481 = order(t207, t1279)
    except:
        t1481 = None
    try:
        t1482 = decrement(t1280)
    except:
        t1482 = None
    try:
        t1483 = get_nth_f(t1281, F0)
    except:
        t1483 = None
    try:
        t1484 = equality(t13, t251)
    except:
        t1484 = None
    try:
        t1485 = chain(t18, merge, t1283)
    except:
        t1485 = None
    try:
        t1486 = replace(t483, t251, t246)
    except:
        t1486 = None
    if t1486 == O:
        return True, f'f76d97a5 - t1486'
    try:
        t1487 = greater(t1284, ONE)
    except:
        t1487 = None
    try:
        t1488 = underfill(I, t2, t1285)
    except:
        t1488 = None
    if t1488 == O:
        return True, f'b8cdaf2b - t1488'
    try:
        t1489 = underfill(t155, t246, t1287)
    except:
        t1489 = None
    if t1489 == O:
        return True, f'10fcaaa3 - t1489'
    try:
        t1490 = gravitate(t6, t1288)
    except:
        t1490 = None
    try:
        t1491 = lefthalf(t1289)
    except:
        t1491 = None
    try:
        t1492 = get_color_rank_t(t1291, F0)
    except:
        t1492 = None
    try:
        t1493 = sfilter_f(t91, t1292)
    except:
        t1493 = None
    try:
        t1494 = compose(t1079, t1293)
    except:
        t1494 = None
    try:
        t1495 = shift(t1294, UNITY)
    except:
        t1495 = None
    try:
        t1496 = interval(ZERO, t1295, TWO)
    except:
        t1496 = None
    try:
        t1497 = cellwise(t492, t1296, ZERO)
    except:
        t1497 = None
    try:
        t1498 = astuple(THREE, ONE)
    except:
        t1498 = None
    try:
        t1499 = canvas(GRAY, UNITY)
    except:
        t1499 = None
    try:
        t1500 = compose(color, t1299)
    except:
        t1500 = None
    try:
        t1501 = f_ofcolor(t148, BLACK)
    except:
        t1501 = None
    try:
        t1502 = color(t327)
    except:
        t1502 = None
    try:
        t1503 = t1087(t769)
    except:
        t1503 = None
    try:
        t1504 = get_rank(t688, F0)
    except:
        t1504 = None
    try:
        t1505 = fill(t437, t300, t1303)
    except:
        t1505 = None
    try:
        t1506 = compose(toindices, t1304)
    except:
        t1506 = None
    try:
        t1507 = sfilter(t9, t1305)
    except:
        t1507 = None
    try:
        t1508 = t1091(t1306)
    except:
        t1508 = None
    try:
        t1509 = matcher(color, BLACK)
    except:
        t1509 = None
    try:
        t1510 = compose(t170, t1309)
    except:
        t1510 = None
    try:
        t1511 = get_nth_f(t1311, F0)
    except:
        t1511 = None
    try:
        t1512 = shift(t1312, TWO_BY_TWO)
    except:
        t1512 = None
    try:
        t1513 = o_g(t1313, R1)
    except:
        t1513 = None
    try:
        t1514 = mapply(t513, t1314)
    except:
        t1514 = None
    try:
        t1515 = matcher(t1315, BLACK)
    except:
        t1515 = None
    try:
        t1516 = fill(t441, BLACK, t1316)
    except:
        t1516 = None
    if t1516 == O:
        return True, f'cce03e0d - t1516'
    try:
        t1517 = halve(t1318)
    except:
        t1517 = None
    try:
        t1518 = fill(I, t246, t1319)
    except:
        t1518 = None
    if t1518 == O:
        return True, f'67385a82 - t1518'
    try:
        t1519 = insert(t22, t1320)
    except:
        t1519 = None
    try:
        t1520 = paint(I, t1322)
    except:
        t1520 = None
    if t1520 == O:
        return True, f'bda2d7a6 - t1520'
    try:
        t1521 = rbind(compose, initset)
    except:
        t1521 = None
    try:
        t1522 = rbind(hmatching, t53)
    except:
        t1522 = None
    try:
        t1523 = apply(t912, t967)
    except:
        t1523 = None
    try:
        t1524 = fork(add, t721, t1327)
    except:
        t1524 = None
    try:
        t1525 = mapply(t139, t1328)
    except:
        t1525 = None
    try:
        t1526 = apply(dedupe, t1330)
    except:
        t1526 = None
    try:
        t1527 = compose(t1115, t1331)
    except:
        t1527 = None
    try:
        t1528 = vconcat(t1332, t1332)
    except:
        t1528 = None
    if t1528 == O:
        return True, f'f5b8619d - t1528'
    try:
        t1529 = fork(shift, identity, t1334)
    except:
        t1529 = None
    try:
        t1530 = compose(t1118, t1335)
    except:
        t1530 = None
    try:
        t1531 = equality(t1119, t1336)
    except:
        t1531 = None
    try:
        t1532 = get_nth_f(t1337, F0)
    except:
        t1532 = None
    try:
        t1533 = mfilter_f(t923, t553)
    except:
        t1533 = None
    try:
        t1534 = corner(t1338, R0)
    except:
        t1534 = None
    try:
        t1535 = corner(t723, R0)
    except:
        t1535 = None
    try:
        t1536 = astuple(t1340, t74)
    except:
        t1536 = None
    try:
        t1537 = paint(I, t1342)
    except:
        t1537 = None
    if t1537 == O:
        return True, f'e76a88a6 - t1537'
    try:
        t1538 = get_nth_f(t725, F0)
    except:
        t1538 = None
    try:
        t1539 = t1128(t1346)
    except:
        t1539 = None
    try:
        t1540 = tojvec(t1347)
    except:
        t1540 = None
    try:
        t1541 = merge(t1348)
    except:
        t1541 = None
    try:
        t1542 = upscale_f(t1351, TWO)
    except:
        t1542 = None
    try:
        t1543 = get_nth_f(t1352, F0)
    except:
        t1543 = None
    try:
        t1544 = shift(t734, t1355)
    except:
        t1544 = None
    try:
        t1545 = normalize(t118)
    except:
        t1545 = None
    try:
        t1546 = paint(t197, t1356)
    except:
        t1546 = None
    try:
        t1547 = vconcat(t363, t1357)
    except:
        t1547 = None
    if t1547 == O:
        return True, f'bd4472b8 - t1547'
    try:
        t1548 = compose(t1359, initset)
    except:
        t1548 = None
    try:
        t1549 = switch(t1360, EIGHT, TWO)
    except:
        t1549 = None
    if t1549 == O:
        return True, f'ce9e57f2 - t1549'
    try:
        t1550 = divide(t1362, THREE)
    except:
        t1550 = None
    try:
        t1551 = compose(t1147, t438)
    except:
        t1551 = None
    try:
        t1552 = astuple(t1148, t1363)
    except:
        t1552 = None
    try:
        t1553 = double(t74)
    except:
        t1553 = None
    try:
        t1554 = mir_rot_t(t1364, R4)
    except:
        t1554 = None
    if t1554 == O:
        return True, f'681b3aeb - t1554'
    try:
        t1555 = decrement(t1151)
    except:
        t1555 = None
    try:
        t1556 = order(t1153, t302)
    except:
        t1556 = None
    try:
        t1557 = paint(I, t1366)
    except:
        t1557 = None
    if t1557 == O:
        return True, f'1f642eb9 - t1557'
    try:
        t1558 = get_arg_rank_f(t1367, size, F0)
    except:
        t1558 = None
    try:
        t1559 = canvas(BLACK, t1368)
    except:
        t1559 = None
    try:
        t1560 = t1157(t721)
    except:
        t1560 = None
    try:
        t1561 = interval(TWO, TEN, ONE)
    except:
        t1561 = None
    try:
        t1562 = apply(color, t490)
    except:
        t1562 = None
    try:
        t1563 = recolor_o(t246, t1370)
    except:
        t1563 = None
    try:
        t1564 = replace(t558, t251, t246)
    except:
        t1564 = None
    if t1564 == O:
        return True, f'1cf80156 - t1564'
    try:
        t1565 = other_f(t758, t1371)
    except:
        t1565 = None
    try:
        t1566 = apply(t175, t1372)
    except:
        t1566 = None
    try:
        t1567 = get_color_rank_f(t180, F0)
    except:
        t1567 = None
    try:
        t1568 = underfill(I, t2, t1374)
    except:
        t1568 = None
    if t1568 == O:
        return True, f'2c608aff - t1568'
    try:
        t1569 = mapply(t386, t1375)
    except:
        t1569 = None
    try:
        t1570 = rbind(colorcount_f, RED)
    except:
        t1570 = None
    try:
        t1571 = paint(I, t1377)
    except:
        t1571 = None
    try:
        t1572 = fill(I, t246, t1378)
    except:
        t1572 = None
    try:
        t1573 = mfilter_f(t7, t1380)
    except:
        t1573 = None
    try:
        t1574 = subtract(t971, t1381)
    except:
        t1574 = None
    try:
        t1575 = compose(t773, t1382)
    except:
        t1575 = None
    try:
        t1576 = replace(t569, t247, t1383)
    except:
        t1576 = None
    if t1576 == O:
        return True, f'5117e062 - t1576'
    try:
        t1577 = get_nth_t(t1384, L1)
    except:
        t1577 = None
    try:
        t1578 = fork(shift, identity, t1387)
    except:
        t1578 = None
    try:
        t1579 = apply(toivec, t1388)
    except:
        t1579 = None
    try:
        t1580 = downscale(t282, t1392)
    except:
        t1580 = None
    try:
        t1581 = mapply(vfrontier, t1393)
    except:
        t1581 = None
    try:
        t1582 = astuple(ONE, THREE)
    except:
        t1582 = None
    try:
        t1583 = colorfilter(t66, ZERO)
    except:
        t1583 = None
    try:
        t1584 = fill(I, t246, t1396)
    except:
        t1584 = None
    try:
        t1585 = compose(t1189, t298)
    except:
        t1585 = None
    try:
        t1586 = vperiod(t99)
    except:
        t1586 = None
    try:
        t1587 = t582(I)
    except:
        t1587 = None
    try:
        t1588 = merge_f(t1402)
    except:
        t1588 = None
    try:
        t1589 = lbind(position, t187)
    except:
        t1589 = None
    try:
        t1590 = equality(t1404, BLACK)
    except:
        t1590 = None
    try:
        t1591 = mir_rot_f(t180, R3)
    except:
        t1591 = None
    try:
        t1592 = fill(t409, t794, t1406)
    except:
        t1592 = None
    if t1592 == O:
        return True, f'bbc9ae5d - t1592'
    try:
        t1593 = mapply(t998, t208)
    except:
        t1593 = None
    try:
        t1594 = power(double, TWO)
    except:
        t1594 = None
    try:
        t1595 = t1409(I)
    except:
        t1595 = None
    try:
        t1596 = f_ofcolor(I, t1410)
    except:
        t1596 = None
    try:
        t1597 = fill(t1205, RED, t1411)
    except:
        t1597 = None
    if t1597 == O:
        return True, f'31aa019c - t1597'
    try:
        t1598 = get_arg_rank_f(t1206, t1412, F0)
    except:
        t1598 = None
    try:
        t1599 = upscale_t(t1413, THREE)
    except:
        t1599 = None
    if t1454 == O:
        return True, f'00d62c1b - t1454'
    try:
        t1600 = get_nth_f(t1414, F0)
    except:
        t1600 = None
    try:
        t1601 = paint(I, t1415)
    except:
        t1601 = None
    if t1601 == O:
        return True, f'8e5a5113 - t1601'
    try:
        t1602 = shift(t1417, UNITY)
    except:
        t1602 = None
    try:
        t1603 = fork(apply, t1418, palette_f)
    except:
        t1603 = None
    try:
        t1604 = mir_rot_t(t1212, R2)
    except:
        t1604 = None
    try:
        t1605 = paint(I, t1421)
    except:
        t1605 = None
    if t1605 == O:
        return True, f'22168020 - t1605'
    try:
        t1606 = t602(t1422)
    except:
        t1606 = None
    try:
        t1607 = rbind(colorcount_f, t1216)
    except:
        t1607 = None
    try:
        t1608 = lbind(matcher, t23)
    except:
        t1608 = None
    try:
        t1609 = interval(ZERO, t1426, NEG_ONE)
    except:
        t1609 = None
    try:
        t1610 = sfilter(t26, t1430)
    except:
        t1610 = None
    try:
        t1611 = mir_rot_t(t1431, R4)
    except:
        t1611 = None
    try:
        t1612 = fork(subtract, t257, t1432)
    except:
        t1612 = None
    try:
        t1613 = lbind(remove, t50)
    except:
        t1613 = None
    try:
        t1614 = combine_f(t1021, t1433)
    except:
        t1614 = None
    try:
        t1615 = subgrid(t1009, I)
    except:
        t1615 = None
    try:
        t1616 = mapply(t435, t1435)
    except:
        t1616 = None
    try:
        t1617 = fork(combine, hfrontier, vfrontier)
    except:
        t1617 = None
    try:
        t1618 = difference(t106, t1437)
    except:
        t1618 = None
    try:
        t1619 = compose(flip, t618)
    except:
        t1619 = None
    try:
        t1620 = index(I, t1439)
    except:
        t1620 = None
    try:
        t1621 = t1028(t1440)
    except:
        t1621 = None
    try:
        t1622 = o_g(t1235, R4)
    except:
        t1622 = None
    try:
        t1623 = lefthalf(t11)
    except:
        t1623 = None
    try:
        t1624 = fill(I, t2, t1443)
    except:
        t1624 = None
    if t1624 == O:
        return True, f'890034e9 - t1624'
    try:
        t1625 = chain(positive, size, t1445)
    except:
        t1625 = None
    try:
        t1626 = rbind(sfilter, t1446)
    except:
        t1626 = None
    try:
        t1627 = paint(t834, t1447)
    except:
        t1627 = None
    if t1627 == O:
        return True, f'd8c310e9 - t1627'
    try:
        t1628 = lbind(shift, t1450)
    except:
        t1628 = None
    try:
        t1629 = mfilter_f(t1244, t1451)
    except:
        t1629 = None
    try:
        t1630 = fork(subtract, t10, t660)
    except:
        t1630 = None
    try:
        t1631 = mir_rot_t(t1453, R2)
    except:
        t1631 = None
    if t1631 == O:
        return True, f'd406998b - t1631'
    try:
        t1632 = chain(toindices, t501, normalize)
    except:
        t1632 = None
    try:
        t1633 = fill(t1252, MAGENTA, t605)
    except:
        t1633 = None
    try:
        t1634 = corner(t638, R2)
    except:
        t1634 = None
    try:
        t1635 = fork(astuple, t1044, t448)
    except:
        t1635 = None
    try:
        t1636 = rbind(add, UP_RIGHT)
    except:
        t1636 = None
    try:
        t1637 = fork(shift, identity, t1460)
    except:
        t1637 = None
    try:
        t1638 = paint(I, t1462)
    except:
        t1638 = None
    if t1638 == O:
        return True, f'363442ee - t1638'
    try:
        t1639 = lbind(greater, t247)
    except:
        t1639 = None
    try:
        t1640 = normalize(t1463)
    except:
        t1640 = None
    try:
        t1641 = fill(I, YELLOW, t1464)
    except:
        t1641 = None
    if t1641 == O:
        return True, f'a5f85a15 - t1641'
    try:
        t1642 = corner(t1466, R0)
    except:
        t1642 = None
    try:
        t1643 = fill(I, t253, t1467)
    except:
        t1643 = None
    if t1643 == O:
        return True, f'623ea044 - t1643'
    try:
        t1644 = inbox(t650)
    except:
        t1644 = None
    try:
        t1645 = fork(mapply, t113, t1469)
    except:
        t1645 = None
    try:
        t1646 = replace(t437, t653, BLACK)
    except:
        t1646 = None
    try:
        t1647 = paint(t48, t1472)
    except:
        t1647 = None
    try:
        t1648 = both(t140, t1473)
    except:
        t1648 = None
    try:
        t1649 = mapply(t470, t1474)
    except:
        t1649 = None
    try:
        t1650 = compose(flip, t1476)
    except:
        t1650 = None
    try:
        t1651 = apply(toindices, t7)
    except:
        t1651 = None
    try:
        t1652 = lefthalf(t1477)
    except:
        t1652 = None
    try:
        t1653 = compose(t1478, t863)
    except:
        t1653 = None
    try:
        t1654 = sfilter_f(t1278, t1480)
    except:
        t1654 = None
    try:
        t1655 = size_t(t1481)
    except:
        t1655 = None
    try:
        t1656 = astuple(t1482, t1482)
    except:
        t1656 = None
    try:
        t1657 = neighbors(t1483)
    except:
        t1657 = None
    try:
        t1658 = branch(t1484, TWO_BY_ZERO, ORIGIN)
    except:
        t1658 = None
    try:
        t1659 = get_arg_rank_t(t315, numcolors_t, L1)
    except:
        t1659 = None
    try:
        t1660 = branch(t1487, BLACK, CYAN)
    except:
        t1660 = None
    try:
        t1661 = sign(t1490)
    except:
        t1661 = None
    try:
        t1662 = apply(t46, t1491)
    except:
        t1662 = None
    try:
        t1663 = multiply(t1290, t74)
    except:
        t1663 = None
    try:
        t1664 = canvas(t1492, UNITY)
    except:
        t1664 = None
    if t1664 == O:
        return True, f'de1cd16c - t1664'
    try:
        t1665 = mapply(neighbors, t73)
    except:
        t1665 = None
    try:
        t1666 = fill(t158, t322, t1493)
    except:
        t1666 = None
    if t1666 == O:
        return True, f'7e0986d6 - t1666'
    try:
        t1667 = t1494(ORIGIN)
    except:
        t1667 = None
    try:
        t1668 = paint(t159, t1495)
    except:
        t1668 = None
    if t1668 == O:
        return True, f'6b9890af - t1668'
    try:
        t1669 = apply(tojvec, t1496)
    except:
        t1669 = None
    try:
        t1670 = downscale(t1497, THREE)
    except:
        t1670 = None
    if t1670 == O:
        return True, f'80af3007 - t1670'
    try:
        t1671 = crop(t1297, DOWN, t1498)
    except:
        t1671 = None
    if t1671 == O:
        return True, f'f8b3ba0a - t1671'
    try:
        t1672 = vconcat(t1298, t1499)
    except:
        t1672 = None
    try:
        t1673 = fork(astuple, t1500, identity)
    except:
        t1673 = None
    try:
        t1674 = intersection(t1085, t1501)
    except:
        t1674 = None
    try:
        t1675 = apply(initset, t427)
    except:
        t1675 = None
    try:
        t1676 = replace(t686, t1300, t1502)
    except:
        t1676 = None
    if t1676 == O:
        return True, f'3de23699 - t1676'
    try:
        t1677 = apply(t687, t1503)
    except:
        t1677 = None
    try:
        t1678 = compose(t1301, t23)
    except:
        t1678 = None
    try:
        t1679 = astuple(t1504, t1089)
    except:
        t1679 = None
    try:
        t1680 = rbind(get_nth_t, F3)
    except:
        t1680 = None
    try:
        t1681 = totuple(t1507)
    except:
        t1681 = None
    try:
        t1682 = fork(shift, identity, t1508)
    except:
        t1682 = None
    try:
        t1683 = compose(flip, t1509)
    except:
        t1683 = None
    try:
        t1684 = fork(mapply, t21, t1510)
    except:
        t1684 = None
    try:
        t1685 = mfilter_f(t1310, t384)
    except:
        t1685 = None
    try:
        t1686 = intersection(t1021, t1433)
    except:
        t1686 = None
    try:
        t1687 = vconcat(t1511, t1511)
    except:
        t1687 = None
    try:
        t1688 = fill(t295, BLACK, t1512)
    except:
        t1688 = None
    try:
        t1689 = merge_f(t1513)
    except:
        t1689 = None
    try:
        t1690 = paint(I, t1514)
    except:
        t1690 = None
    try:
        t1691 = lbind(add, NEG_UNITY)
    except:
        t1691 = None
    try:
        t1692 = dneighbors(t1517)
    except:
        t1692 = None
    try:
        t1693 = chain(numcolors_t, lefthalf, tophalf)
    except:
        t1693 = None
    try:
        t1694 = difference(t26, t1109)
    except:
        t1694 = None
    try:
        t1695 = lbind(rbind, adjacent)
    except:
        t1695 = None
    try:
        t1696 = fork(either, t1324, t1522)
    except:
        t1696 = None
    try:
        t1697 = subtract(NINE, t150)
    except:
        t1697 = None
    try:
        t1698 = fork(astuple, t913, t1524)
    except:
        t1698 = None
    try:
        t1699 = paint(t343, t1525)
    except:
        t1699 = None
    if t1699 == O:
        return True, f'178fcbfb - t1699'
    try:
        t1700 = extract(t1329, t23)
    except:
        t1700 = None
    try:
        t1701 = t345(t1526)
    except:
        t1701 = None
    if t1701 == O:
        return True, f'4be741c5 - t1701'
    try:
        t1702 = fork(sfilter, t10, t1527)
    except:
        t1702 = None
    try:
        t1703 = replace(t717, t251, t246)
    except:
        t1703 = None
    if t1703 == O:
        return True, f'0520fde7 - t1703'
    try:
        t1704 = mapply(t1529, t9)
    except:
        t1704 = None
    try:
        t1705 = initset(t1530)
    except:
        t1705 = None
    try:
        t1706 = fill(t920, t246, t126)
    except:
        t1706 = None
    try:
        t1707 = fork(subtract, identity, crement)
    except:
        t1707 = None
    try:
        t1708 = lbind(shift, t1532)
    except:
        t1708 = None
    try:
        t1709 = rbind(adjacent, t1533)
    except:
        t1709 = None
    try:
        t1710 = shoot(t1534, NEG_UNITY)
    except:
        t1710 = None
    try:
        t1711 = invert(t1535)
    except:
        t1711 = None
    try:
        t1712 = crop(t1123, DOWN, t1536)
    except:
        t1712 = None
    try:
        t1713 = crop(I, t833, THREE_BY_THREE)
    except:
        t1713 = None
    try:
        t1714 = center(t1538)
    except:
        t1714 = None
    try:
        t1715 = compose(t1345, t10)
    except:
        t1715 = None
    try:
        t1716 = t727(t1539)
    except:
        t1716 = None
    try:
        t1717 = shift(t188, t1540)
    except:
        t1717 = None
    try:
        t1718 = t1131(t1541)
    except:
        t1718 = None
    try:
        t1719 = upscale_f(t1542, TWO)
    except:
        t1719 = None
    try:
        t1720 = equality(t794, t247)
    except:
        t1720 = None
    try:
        t1721 = shift(t1543, LEFT)
    except:
        t1721 = None
    try:
        t1722 = lbind(shift, t1344)
    except:
        t1722 = None
    try:
        t1723 = fill(I, RED, t1544)
    except:
        t1723 = None
    try:
        t1724 = t937(t1545)
    except:
        t1724 = None
    try:
        t1725 = bottomhalf(t48)
    except:
        t1725 = None
    try:
        t1726 = fork(vconcat, t1358, t1229)
    except:
        t1726 = None
    try:
        t1727 = apply(t1279, t7)
    except:
        t1727 = None
    try:
        t1728 = compose(t1143, t1548)
    except:
        t1728 = None
    try:
        t1729 = rbind(subgrid, t1145)
    except:
        t1729 = None
    try:
        t1730 = downscale(t1146, t1550)
    except:
        t1730 = None
    if t1730 == O:
        return True, f'5ad4f10b - t1730'
    try:
        t1731 = paint(t744, t1054)
    except:
        t1731 = None
    try:
        t1732 = fork(sfilter, identity, t1551)
    except:
        t1732 = None
    try:
        t1733 = mir_rot_t(t1148, R5)
    except:
        t1733 = None
    try:
        t1734 = divide(t1553, t549)
    except:
        t1734 = None
    try:
        t1735 = tojvec(t1555)
    except:
        t1735 = None
    try:
        t1736 = get_nth_t(t1556, L1)
    except:
        t1736 = None
    try:
        t1737 = color(t1558)
    except:
        t1737 = None
    try:
        t1738 = hconcat(t951, t1559)
    except:
        t1738 = None
    if t1738 == O:
        return True, f'1fad071e - t1738'
    try:
        t1739 = mapply(delta, t755)
    except:
        t1739 = None
    try:
        t1740 = prapply(astuple, t1561, t1561)
    except:
        t1740 = None
    try:
        t1741 = get_nth_f(t1562, F0)
    except:
        t1741 = None
    try:
        t1742 = paint(I, t1563)
    except:
        t1742 = None
    try:
        t1743 = canvas(t1565, UNITY)
    except:
        t1743 = None
    if t1743 == O:
        return True, f'd9fac9be - t1743'
    try:
        t1744 = mir_rot_t(t1566, R3)
    except:
        t1744 = None
    try:
        t1745 = replace(t958, t2, t1567)
    except:
        t1745 = None
    if t1745 == O:
        return True, f'47c1f68c - t1745'
    try:
        t1746 = o_g(t762, R1)
    except:
        t1746 = None
    try:
        t1747 = paint(I, t1569)
    except:
        t1747 = None
    if t1747 == O:
        return True, f'8eb1be9a - t1747'
    try:
        t1748 = get_arg_rank_f(t1376, t1570, F0)
    except:
        t1748 = None
    try:
        t1749 = mapply(ineighbors, t6)
    except:
        t1749 = None
    try:
        t1750 = shift(t1377, UP_RIGHT)
    except:
        t1750 = None
    try:
        t1751 = subgrid(t427, t3)
    except:
        t1751 = None
    try:
        t1752 = fill(I, GRAY, t1573)
    except:
        t1752 = None
    try:
        t1753 = astuple(ONE, t1574)
    except:
        t1753 = None
    try:
        t1754 = sfilter_f(t568, t1575)
    except:
        t1754 = None
    try:
        t1755 = astuple(t972, t1577)
    except:
        t1755 = None
    try:
        t1756 = order(t1385, t342)
    except:
        t1756 = None
    try:
        t1757 = box(t219)
    except:
        t1757 = None
    try:
        t1758 = t823(THREE)
    except:
        t1758 = None
    try:
        t1759 = mpapply(shift, t978, t1579)
    except:
        t1759 = None
    try:
        t1760 = compose(t586, t398)
    except:
        t1760 = None
    try:
        t1761 = f_ofcolor(t1580, BLACK)
    except:
        t1761 = None
    try:
        t1762 = size_f(t1581)
    except:
        t1762 = None
    try:
        t1763 = initset(t1582)
    except:
        t1763 = None
    try:
        t1764 = difference(t66, t1583)
    except:
        t1764 = None
    try:
        t1765 = mapply(t1585, t207)
    except:
        t1765 = None
    try:
        t1766 = get_color_rank_t(t5, L1)
    except:
        t1766 = None
    try:
        t1767 = toivec(t1586)
    except:
        t1767 = None
    try:
        t1768 = rbind(intersection, t54)
    except:
        t1768 = None
    try:
        t1769 = t1401(t1587)
    except:
        t1769 = None
    try:
        t1770 = apply(t1194, t967)
    except:
        t1770 = None
    try:
        t1771 = width_f(t1588)
    except:
        t1771 = None
    try:
        t1772 = chain(t1196, t1403, t1589)
    except:
        t1772 = None
    try:
        t1773 = branch(t1590, LEFT, RIGHT)
    except:
        t1773 = None
    try:
        t1774 = compose(t721, t10)
    except:
        t1774 = None
    try:
        t1775 = paint(t1405, t1591)
    except:
        t1775 = None
    if t1775 == O:
        return True, f'11852cab - t1775'
    try:
        t1776 = underpaint(I, t1593)
    except:
        t1776 = None
    if t1776 == O:
        return True, f'444801d8 - t1776'
    try:
        t1777 = branch(t999, t714, t72)
    except:
        t1777 = None
    try:
        t1778 = rbind(adjacent, t1596)
    except:
        t1778 = None
    try:
        t1779 = remove(t1598, t1206)
    except:
        t1779 = None
    try:
        t1780 = position(t1208, t1414)
    except:
        t1780 = None
    try:
        t1781 = sfilter_f(t1416, t217)
    except:
        t1781 = None
    try:
        t1782 = paint(t71, t1602)
    except:
        t1782 = None
    if t1782 == O:
        return True, f'137eaa0f - t1782'
    try:
        t1783 = compose(t65, t1603)
    except:
        t1783 = None
    try:
        t1784 = branch(t805, t1420, t1604)
    except:
        t1784 = None
    try:
        t1785 = matcher(t602, t1606)
    except:
        t1785 = None
    try:
        t1786 = f_ofcolor(t148, t251)
    except:
        t1786 = None
    try:
        t1787 = matcher(t1423, t503)
    except:
        t1787 = None
    try:
        t1788 = chain(t425, t1217, t1608)
    except:
        t1788 = None
    try:
        t1789 = branch(t1425, t18, identity)
    except:
        t1789 = None
    try:
        t1790 = apply(t811, t1609)
    except:
        t1790 = None
    try:
        t1791 = intersection(t1428, t1433)
    except:
        t1791 = None
    try:
        t1792 = extract(t122, t1014)
    except:
        t1792 = None
    try:
        t1793 = fill(I, t253, t1610)
    except:
        t1793 = None
    try:
        t1794 = width_t(t255)
    except:
        t1794 = None
    try:
        t1795 = product(t171, t508)
    except:
        t1795 = None
    try:
        t1796 = fork(shoot, t257, t1612)
    except:
        t1796 = None
    try:
        t1797 = chain(size, t1613, palette_t)
    except:
        t1797 = None
    try:
        t1798 = width_t(t1615)
    except:
        t1798 = None
    try:
        t1799 = compose(t1434, t55)
    except:
        t1799 = None
    try:
        t1800 = fill(t437, t246, t1616)
    except:
        t1800 = None
    if t1800 == O:
        return True, f'd5d6de2d - t1800'
    try:
        t1801 = toindices(t616)
    except:
        t1801 = None
    try:
        t1802 = move(I, t1618, RIGHT)
    except:
        t1802 = None
    if t1802 == O:
        return True, f'025d127b - t1802'
    try:
        t1803 = mfilter_f(t7, t1619)
    except:
        t1803 = None
    try:
        t1804 = replace(t825, t251, t246)
    except:
        t1804 = None
    if t1804 == O:
        return True, f'017c7c7b - t1804'
    try:
        t1805 = f_ofcolor(t86, t50)
    except:
        t1805 = None
    try:
        t1806 = lbind(recolor_i, t1620)
    except:
        t1806 = None
    try:
        t1807 = fill(I, t2, t1621)
    except:
        t1807 = None
    try:
        t1808 = colorfilter(t1622, ZERO)
    except:
        t1808 = None
    try:
        t1809 = f_ofcolor(t1623, ORANGE)
    except:
        t1809 = None
    try:
        t1810 = fork(both, t1033, t1625)
    except:
        t1810 = None
    try:
        t1811 = chain(t626, t1626, normalize)
    except:
        t1811 = None
    try:
        t1812 = fill(I, t246, t1629)
    except:
        t1812 = None
    if t1812 == O:
        return True, f'810b9b61 - t1812'
    try:
        t1813 = compose(t839, t1630)
    except:
        t1813 = None
    try:
        t1814 = matcher(t10, RED)
    except:
        t1814 = None
    try:
        t1815 = mfilter_f(t1456, t384)
    except:
        t1815 = None
    try:
        t1816 = chain(size, t1251, t1632)
    except:
        t1816 = None
    try:
        t1817 = shoot(t1634, DOWN_LEFT)
    except:
        t1817 = None
    try:
        t1818 = product(t54, t54)
    except:
        t1818 = None
    try:
        t1819 = apply(color, t301)
    except:
        t1819 = None
    try:
        t1820 = get_color_rank_f(t126, F0)
    except:
        t1820 = None
    try:
        t1821 = lbind(shift, t1640)
    except:
        t1821 = None
    try:
        t1822 = branch(t1262, t190, t19)
    except:
        t1822 = None
    try:
        t1823 = subgrid(t1466, t1263)
    except:
        t1823 = None
    try:
        t1824 = lbind(contained, ZERO)
    except:
        t1824 = None
    try:
        t1825 = t853(THREE)
    except:
        t1825 = None
    try:
        t1826 = get_color_rank_t(t1646, L1)
    except:
        t1826 = None
    try:
        t1827 = o_g(t1647, R5)
    except:
        t1827 = None
    try:
        t1828 = fill(I, t246, t1649)
    except:
        t1828 = None
    try:
        t1829 = sfilter_f(t1060, t1650)
    except:
        t1829 = None
    try:
        t1830 = product(t125, t125)
    except:
        t1830 = None
    try:
        t1831 = interval(ZERO, FIVE, ONE)
    except:
        t1831 = None
    try:
        t1832 = palette_t(t1652)
    except:
        t1832 = None
    try:
        t1833 = fork(sfilter, t1276, t1653)
    except:
        t1833 = None
    try:
        t1834 = mapply(t475, t1654)
    except:
        t1834 = None
    try:
        t1835 = interval(ZERO, t1655, ONE)
    except:
        t1835 = None
    try:
        t1836 = canvas(t50, t1656)
    except:
        t1836 = None
    try:
        t1837 = colorfilter(t9, BURGUNDY)
    except:
        t1837 = None
    try:
        t1838 = fill(I, t246, t1657)
    except:
        t1838 = None
    if t1838 == O:
        return True, f'67a423a3 - t1838'
    try:
        t1839 = t1485(t1659)
    except:
        t1839 = None
    try:
        t1840 = canvas(t1660, UNITY)
    except:
        t1840 = None
    if t1840 == O:
        return True, f'239be575 - t1840'
    try:
        t1841 = gravitate(t1288, t6)
    except:
        t1841 = None
    try:
        t1842 = rbind(order, invert)
    except:
        t1842 = None
    try:
        t1843 = double(t1663)
    except:
        t1843 = None
    try:
        t1844 = fill(t878, t300, t1665)
    except:
        t1844 = None
    try:
        t1845 = fill(I, t246, t1667)
    except:
        t1845 = None
    try:
        t1846 = fill(t160, t246, t1669)
    except:
        t1846 = None
    try:
        t1847 = asobject(t1672)
    except:
        t1847 = None
    try:
        t1848 = fill(t325, t246, t1674)
    except:
        t1848 = None
    if t1848 == O:
        return True, f'1b2d62fb - t1848'
    try:
        t1849 = lbind(t193, t1675)
    except:
        t1849 = None
    try:
        t1850 = mapply(t328, t1677)
    except:
        t1850 = None
    try:
        t1851 = sfilter_f(t79, t1678)
    except:
        t1851 = None
    try:
        t1852 = connect(t1302, t1679)
    except:
        t1852 = None
    try:
        t1853 = c_zo_n(S, t1, t1680)
    except:
        t1853 = None
    try:
        t1854 = lbind(mapply, t1617)
    except:
        t1854 = None
    try:
        t1855 = apply(color, t1681)
    except:
        t1855 = None
    try:
        t1856 = chain(t61, t21, t1682)
    except:
        t1856 = None
    try:
        t1857 = extract(t1307, t1683)
    except:
        t1857 = None
    try:
        t1858 = fill(I, t246, t1685)
    except:
        t1858 = None
    try:
        t1859 = fill(t696, BLACK, t1686)
    except:
        t1859 = None
    if t1859 == O:
        return True, f'ce4f8723 - t1859'
    try:
        t1860 = vconcat(t1511, t1687)
    except:
        t1860 = None
    if t1860 == O:
        return True, f'3ac3eb23 - t1860'
    try:
        t1861 = get_color_rank_t(t1688, L1)
    except:
        t1861 = None
    try:
        t1862 = get_color_rank_f(t1689, F0)
    except:
        t1862 = None
    try:
        t1863 = f_ofcolor(I, FOUR)
    except:
        t1863 = None
    try:
        t1864 = chain(flip, t1515, t1691)
    except:
        t1864 = None
    try:
        t1865 = insert(t1517, t1692)
    except:
        t1865 = None
    try:
        t1866 = get_arg_rank_f(t1519, t1693, F1)
    except:
        t1866 = None
    try:
        t1867 = fill(t1321, BLACK, t1694)
    except:
        t1867 = None
    if t1867 == O:
        return True, f'25d8a9c8 - t1867'
    try:
        t1868 = fork(difference, identity, t1323)
    except:
        t1868 = None
    try:
        t1869 = sfilter_f(t125, t1696)
    except:
        t1869 = None
    try:
        t1870 = astuple(ONE, t1697)
    except:
        t1870 = None
    try:
        t1871 = lbind(intersection, t29)
    except:
        t1871 = None
    try:
        t1872 = get_arg_rank_f(t1519, t1693, F0)
    except:
        t1872 = None
    try:
        t1873 = compose(box, t1698)
    except:
        t1873 = None
    try:
        t1874 = get_nth_t(t1700, F0)
    except:
        t1874 = None
    if t1874 == O:
        return True, f'72ca375d - t1874'
    try:
        t1875 = paint(t348, t1704)
    except:
        t1875 = None
    if t1875 == O:
        return True, f'1caeab9d - t1875'
    try:
        t1876 = lbind(rapply, t1705)
    except:
        t1876 = None
    try:
        t1877 = fork(add, identity, t1707)
    except:
        t1877 = None
    try:
        t1878 = compose(t1708, tojvec)
    except:
        t1878 = None
    try:
        t1879 = mfilter_f(t206, t1709)
    except:
        t1879 = None
    try:
        t1880 = shoot(t1534, UNITY)
    except:
        t1880 = None
    try:
        t1881 = shift(t6, t1711)
    except:
        t1881 = None
    try:
        t1882 = vconcat(t1123, t1712)
    except:
        t1882 = None
    if t1882 == O:
        return True, f'eb281b96 - t1882'
    try:
        t1883 = astuple(t1343, t1713)
    except:
        t1883 = None
    try:
        t1884 = shift(t1344, t1714)
    except:
        t1884 = None
    try:
        t1885 = rbind(sfilter, t1715)
    except:
        t1885 = None
    try:
        t1886 = mir_rot_t(t1716, R1)
    except:
        t1886 = None
    if t1874 == O:
        return True, f'd56f2372 - t1874'
    try:
        t1887 = fill(I, CYAN, t1717)
    except:
        t1887 = None
    if t1887 == O:
        return True, f'760b3cac - t1887'
    try:
        t1888 = rbind(interval, t1718)
    except:
        t1888 = None
    try:
        t1889 = multiply(DOWN_LEFT, t1151)
    except:
        t1889 = None
    try:
        t1890 = get_arg_rank_f(t933, size, F0)
    except:
        t1890 = None
    try:
        t1891 = shape_f(t1719)
    except:
        t1891 = None
    try:
        t1892 = lbind(shift, t1721)
    except:
        t1892 = None
    try:
        t1893 = chain(t276, t298, t1309)
    except:
        t1893 = None
    try:
        t1894 = f_ofcolor(t1723, RED)
    except:
        t1894 = None
    try:
        t1895 = matcher(t10, t1724)
    except:
        t1895 = None
    try:
        t1896 = merge_f(t682)
    except:
        t1896 = None
    try:
        t1897 = t738(t1725)
    except:
        t1897 = None
    if t1848 == O:
        return True, f'e345f17b - t1848'
    try:
        t1898 = fork(vconcat, t364, t1726)
    except:
        t1898 = None
    try:
        t1899 = apply(t941, t1727)
    except:
        t1899 = None
    try:
        t1900 = mapply(t1728, t54)
    except:
        t1900 = None
    try:
        t1901 = chain(t1361, t233, t1729)
    except:
        t1901 = None
    try:
        t1902 = mir_rot_t(t1731, R0)
    except:
        t1902 = None
    if t1902 == O:
        return True, f'feca6190 - t1902'
    try:
        t1903 = compose(dneighbors, t23)
    except:
        t1903 = None
    try:
        t1904 = mir_rot_t(t1148, R6)
    except:
        t1904 = None
    try:
        t1905 = increment(t1734)
    except:
        t1905 = None
    try:
        t1906 = connect(ORIGIN, t1735)
    except:
        t1906 = None
    try:
        t1907 = color(t1736)
    except:
        t1907 = None
    try:
        t1908 = toindices(t1558)
    except:
        t1908 = None
    try:
        t1909 = t1157(t713)
    except:
        t1909 = None
    try:
        t1910 = fill(t1158, t264, t1739)
    except:
        t1910 = None
    if t1910 == O:
        return True, f'543a7ed5 - t1910'
    try:
        t1911 = mapply(t1369, t1740)
    except:
        t1911 = None
    try:
        t1912 = equality(t1160, t1741)
    except:
        t1912 = None
    try:
        t1913 = papply(pair, t1566, t1744)
    except:
        t1913 = None
    try:
        t1914 = matcher(t10, GREEN)
    except:
        t1914 = None
    try:
        t1915 = mapply(t435, t1746)
    except:
        t1915 = None
    try:
        t1916 = subgrid(t1748, I)
    except:
        t1916 = None
    if t1916 == O:
        return True, f'e50d258f - t1916'
    try:
        t1917 = fill(t966, t246, t1749)
    except:
        t1917 = None
    if t1917 == O:
        return True, f'0ca9ddb6 - t1917'
    try:
        t1918 = paint(t1571, t1750)
    except:
        t1918 = None
    try:
        t1919 = branch(t1379, t1751, t969)
    except:
        t1919 = None
    if t1919 == O:
        return True, f'ff805c23 - t1919'
    try:
        t1920 = canvas(CYAN, t1753)
    except:
        t1920 = None
    try:
        t1921 = apply(merge, t1754)
    except:
        t1921 = None
    try:
        t1922 = connect(t1755, t1384)
    except:
        t1922 = None
    try:
        t1923 = apply(color, t1756)
    except:
        t1923 = None
    try:
        t1924 = difference(t1757, t219)
    except:
        t1924 = None
    try:
        t1925 = mapply(t1578, t1758)
    except:
        t1925 = None
    try:
        t1926 = paint(t130, t1759)
    except:
        t1926 = None
    try:
        t1927 = fork(equality, t1760, t586)
    except:
        t1927 = None
    try:
        t1928 = fill(t399, BLACK, t1761)
    except:
        t1928 = None
    if t1928 == O:
        return True, f'6ecd11f4 - t1928'
    try:
        t1929 = extract(t880, t553)
    except:
        t1929 = None
    try:
        t1930 = mapply(hfrontier, t1393)
    except:
        t1930 = None
    try:
        t1931 = insert(t1394, t1763)
    except:
        t1931 = None
    try:
        t1932 = remove_f(t1395, t1764)
    except:
        t1932 = None
    try:
        t1933 = paint(I, t1765)
    except:
        t1933 = None
    if t1933 == O:
        return True, f'c444b776 - t1933'
    try:
        t1934 = replace(t1399, t226, t1766)
    except:
        t1934 = None
    try:
        t1935 = lbind(multiply, t1767)
    except:
        t1935 = None
    try:
        t1936 = lbind(mapply, dneighbors)
    except:
        t1936 = None
    if t1848 == O:
        return True, f'f2829549 - t1848'
    try:
        t1937 = f_ofcolor(t1769, CYAN)
    except:
        t1937 = None
    try:
        t1938 = rbind(intersection, t790)
    except:
        t1938 = None
    try:
        t1939 = width_f(t791)
    except:
        t1939 = None
    try:
        t1940 = mapply(box, t957)
    except:
        t1940 = None
    try:
        t1941 = compose(t587, t1772)
    except:
        t1941 = None
    try:
        t1942 = rbind(shoot, t1773)
    except:
        t1942 = None
    try:
        t1943 = compose(t298, t233)
    except:
        t1943 = None
    try:
        t1944 = mfilter_f(t207, t1778)
    except:
        t1944 = None
    try:
        t1945 = rbind(contained, t1779)
    except:
        t1945 = None
    try:
        t1946 = subgrid(t427, I)
    except:
        t1946 = None
    try:
        t1947 = shoot(t1600, t1780)
    except:
        t1947 = None
    try:
        t1948 = apply(t1210, t1781)
    except:
        t1948 = None
    try:
        t1949 = rbind(get_rank, L1)
    except:
        t1949 = None
    try:
        t1950 = chain(t1521, t1084, initset)
    except:
        t1950 = None
    try:
        t1951 = asobject(t1784)
    except:
        t1951 = None
    if t1848 == O:
        return True, f'66f2d22f - t1848'
    try:
        t1952 = extract(t422, t1785)
    except:
        t1952 = None
    try:
        t1953 = combine_f(t1214, t1786)
    except:
        t1953 = None
    try:
        t1954 = lbind(apply, t1787)
    except:
        t1954 = None
    try:
        t1955 = t1788(ZERO)
    except:
        t1955 = None
    try:
        t1956 = t1789(t809)
    except:
        t1956 = None
    try:
        t1957 = pair(t1220, t1790)
    except:
        t1957 = None
    try:
        t1958 = fork(intersection, t10, t23)
    except:
        t1958 = None
    try:
        t1959 = fill(t250, t246, t1791)
    except:
        t1959 = None
    if t1959 == O:
        return True, f'94f9d214 - t1959'
    try:
        t1960 = asobject(t1792)
    except:
        t1960 = None
    try:
        t1961 = intersection(t252, t1015)
    except:
        t1961 = None
    try:
        t1962 = increment(t609)
    except:
        t1962 = None
    try:
        t1963 = vsplit(t1611, t1794)
    except:
        t1963 = None
    try:
        t1964 = apply(t1018, t1795)
    except:
        t1964 = None
    try:
        t1965 = difference(t1614, t1686)
    except:
        t1965 = None
    try:
        t1966 = halve(t1798)
    except:
        t1966 = None
    try:
        t1967 = extract(t9, t1799)
    except:
        t1967 = None
    try:
        t1968 = mapply(t1617, t1801)
    except:
        t1968 = None
    try:
        t1969 = fill(t1026, t246, t1803)
    except:
        t1969 = None
    if t1969 == O:
        return True, f'd2abd087 - t1969'
    try:
        t1970 = difference(t1438, t1805)
    except:
        t1970 = None
    try:
        t1971 = power(t1028, TWO)
    except:
        t1971 = None
    try:
        t1972 = get_nth_f(t1808, F0)
    except:
        t1972 = None
    try:
        t1973 = fill(t1442, ORANGE, t1809)
    except:
        t1973 = None
    if t1973 == O:
        return True, f'a68b268e - t1973'
    try:
        t1974 = chain(t1521, t1359, initset)
    except:
        t1974 = None
    try:
        t1975 = mfilter_f(t832, t1810)
    except:
        t1975 = None
    try:
        t1976 = apply(t298, t115)
    except:
        t1976 = None
    try:
        t1977 = lbind(compose, t1813)
    except:
        t1977 = None
    try:
        t1978 = compose(flip, t1814)
    except:
        t1978 = None
    try:
        t1979 = underfill(I, t246, t1815)
    except:
        t1979 = None
    if t1979 == O:
        return True, f'dbc1a6ce - t1979'
    try:
        t1980 = astuple(t185, ONE)
    except:
        t1980 = None
    try:
        t1981 = get_arg_rank_t(t635, t1816, F0)
    except:
        t1981 = None
    try:
        t1982 = fill(t1633, ORANGE, t810)
    except:
        t1982 = None
    if t1982 == O:
        return True, f'd364b489 - t1982'
    try:
        t1983 = combine(t1458, t1817)
    except:
        t1983 = None
    try:
        t1984 = apply(t1635, t1818)
    except:
        t1984 = None
    try:
        t1985 = rbind(contained, t1819)
    except:
        t1985 = None
    try:
        t1986 = replace(t846, t247, t300)
    except:
        t1986 = None
    try:
        t1987 = rbind(colorcount_f, t1820)
    except:
        t1987 = None
    if t1959 == O:
        return True, f'6430c8c4 - t1959'
    try:
        t1988 = apply(t1210, t729)
    except:
        t1988 = None
    try:
        t1989 = crop(I, ORIGIN, t1822)
    except:
        t1989 = None
    try:
        t1990 = height_t(t1823)
    except:
        t1990 = None
    try:
        t1991 = center(t465)
    except:
        t1991 = None
    if t1959 == O:
        return True, f'0c9aba6e - t1959'
    try:
        t1992 = matcher(numcolors_f, BLUE)
    except:
        t1992 = None
    try:
        t1993 = fill(t1267, t264, t1825)
    except:
        t1993 = None
    try:
        t1994 = box(t106)
    except:
        t1994 = None
    try:
        t1995 = merge_f(t1827)
    except:
        t1995 = None
    try:
        t1996 = branch(t1648, t586, t302)
    except:
        t1996 = None
    try:
        t1997 = get_nth_t(t857, L1)
    except:
        t1997 = None
    try:
        t1998 = normalize(t1829)
    except:
        t1998 = None
    try:
        t1999 = apply(double, t1831)
    except:
        t1999 = None
    try:
        t2000 = other_f(t1832, BLACK)
    except:
        t2000 = None
    try:
        t2001 = paint(I, t1834)
    except:
        t2001 = None
    if t2001 == O:
        return True, f'ddf7fa4f - t2001'
    try:
        t2002 = pair(t1481, t1835)
    except:
        t2002 = None
    try:
        t2003 = mapply(outbox, t1837)
    except:
        t2003 = None
    try:
        t2004 = equality(t13, t247)
    except:
        t2004 = None
    try:
        t2005 = t1485(t1839)
    except:
        t2005 = None
    try:
        t2006 = get_nth_f(t1841, F0)
    except:
        t2006 = None
    try:
        t2007 = righthalf(t1289)
    except:
        t2007 = None
    try:
        t2008 = add(t1076, t1843)
    except:
        t2008 = None
    if t1959 == O:
        return True, f'fafffa47 - t1959'
    try:
        t2009 = hsplit(t1846, THREE)
    except:
        t2009 = None
    try:
        t2010 = lbind(shift, t1847)
    except:
        t2010 = None
    try:
        t2011 = outbox(t126)
    except:
        t2011 = None
    try:
        t2012 = paint(I, t1850)
    except:
        t2012 = None
    try:
        t2013 = fill(I, t246, t1851)
    except:
        t2013 = None
    if t2013 == O:
        return True, f'ba26e723 - t2013'
    try:
        t2014 = shift(t6, UP_RIGHT)
    except:
        t2014 = None
    try:
        t2015 = compose(t1854, toindices)
    except:
        t2015 = None
    try:
        t2016 = apply(center, t1681)
    except:
        t2016 = None
    try:
        t2017 = palette_f(t1857)
    except:
        t2017 = None
    try:
        t2018 = fork(compose, t10, t23)
    except:
        t2018 = None
    try:
        t2019 = fill(t1858, CYAN, t73)
    except:
        t2019 = None
    if t2019 == O:
        return True, f'253bf280 - t2019'
    try:
        t2020 = other_f(t123, t1861)
    except:
        t2020 = None
    try:
        t2021 = matcher(t10, t1862)
    except:
        t2021 = None
    try:
        t2022 = get_nth_f(t1863, F0)
    except:
        t2022 = None
    try:
        t2023 = fork(both, t1515, t1864)
    except:
        t2023 = None
    try:
        t2024 = replace(t1317, t251, t264)
    except:
        t2024 = None
    if t2024 == O:
        return True, f'7b6016b9 - t2024'
    try:
        t2025 = fill(I, t246, t1865)
    except:
        t2025 = None
    if t2025 == O:
        return True, f'e9614598 - t2025'
    try:
        t2026 = mir_rot_t(t1866, R2)
    except:
        t2026 = None
    try:
        t2027 = chain(t1521, t1695, t1868)
    except:
        t2027 = None
    try:
        t2028 = mapply(t709, t1869)
    except:
        t2028 = None
    try:
        t2029 = canvas(BLACK, t1870)
    except:
        t2029 = None
    try:
        t2030 = compose(size, t1871)
    except:
        t2030 = None
    try:
        t2031 = mir_rot_t(t1872, R2)
    except:
        t2031 = None
    try:
        t2032 = compose(increment, t298)
    except:
        t2032 = None
    try:
        t2033 = recolor_o(t264, t599)
    except:
        t2033 = None
    try:
        t2034 = chain(initset, t10, t1876)
    except:
        t2034 = None
    try:
        t2035 = branch(t1531, identity, t1877)
    except:
        t2035 = None
    try:
        t2036 = rbind(multiply, THREE)
    except:
        t2036 = None
    try:
        t2037 = fill(I, t246, t1879)
    except:
        t2037 = None
    if t2037 == O:
        return True, f'b2862040 - t2037'
    try:
        t2038 = combine(t1710, t1880)
    except:
        t2038 = None
    try:
        t2039 = apply(t1339, t1881)
    except:
        t2039 = None
    try:
        t2040 = combine_t(t927, t1883)
    except:
        t2040 = None
    try:
        t2041 = shift(t1884, NEG_UNITY)
    except:
        t2041 = None
    try:
        t2042 = chain(t1885, vfrontier, center)
    except:
        t2042 = None
    try:
        t2043 = t727(t1886)
    except:
        t2043 = None
    if t2043 == O:
        return True, f'eb5a1d5d - t2043'
    try:
        t2044 = width_t(t523)
    except:
        t2044 = None
    try:
        t2045 = f_ofcolor(I, t1349)
    except:
        t2045 = None
    try:
        t2046 = fill(t1350, t300, t1890)
    except:
        t2046 = None
    try:
        t2047 = shift(t1719, t1891)
    except:
        t2047 = None
    try:
        t2048 = equality(t794, t251)
    except:
        t2048 = None
    try:
        t2049 = vperiod(t1721)
    except:
        t2049 = None
    try:
        t2050 = apply(t298, t725)
    except:
        t2050 = None
    try:
        t2051 = mir_rot_f(t1894, R0)
    except:
        t2051 = None
    try:
        t2052 = sfilter_f(t1545, t1895)
    except:
        t2052 = None
    try:
        t2053 = fill(t1138, t264, t1896)
    except:
        t2053 = None
    try:
        t2054 = paint(t1546, t1897)
    except:
        t2054 = None
    try:
        t2055 = fill(I, t246, t1899)
    except:
        t2055 = None
    if t2055 == O:
        return True, f'54d82841 - t2055'
    try:
        t2056 = fill(t200, GRAY, t1900)
    except:
        t2056 = None
    if t2056 == O:
        return True, f'a48eeaf7 - t2056'
    try:
        t2057 = rbind(chain, t1903)
    except:
        t2057 = None
    try:
        t2058 = astuple(t1733, t1904)
    except:
        t2058 = None
    try:
        t2059 = repeat(t1149, t1905)
    except:
        t2059 = None
    try:
        t2060 = insert(UNITY, t1906)
    except:
        t2060 = None
    try:
        t2061 = prapply(connect, t1908, t1908)
    except:
        t2061 = None
    try:
        t2062 = hconcat(t1560, t1909)
    except:
        t2062 = None
    try:
        t2063 = get_arg_rank_f(t1911, size, F0)
    except:
        t2063 = None
    try:
        t2064 = color(t378)
    except:
        t2064 = None
    try:
        t2065 = apply(t175, t1913)
    except:
        t2065 = None
    try:
        t2066 = sfilter_f(t761, t1914)
    except:
        t2066 = None
    try:
        t2067 = fill(t762, t246, t1915)
    except:
        t2067 = None
    try:
        t2068 = col_row(t564, R1)
    except:
        t2068 = None
    try:
        t2069 = shift(t1377, DOWN_LEFT)
    except:
        t2069 = None
    try:
        t2070 = difference(t770, t1171)
    except:
        t2070 = None
    try:
        t2071 = paint(t1752, t129)
    except:
        t2071 = None
    if t2071 == O:
        return True, f'63613498 - t2071'
    try:
        t2072 = subtract(SIX, t1574)
    except:
        t2072 = None
    try:
        t2073 = mapply(delta, t1921)
    except:
        t2073 = None
    try:
        t2074 = connect(t1755, t774)
    except:
        t2074 = None
    try:
        t2075 = repeat(t1923, BLUE)
    except:
        t2075 = None
    try:
        t2076 = lbind(shift, t1924)
    except:
        t2076 = None
    try:
        t2077 = paint(t220, t1925)
    except:
        t2077 = None
    try:
        t2078 = mir_rot_t(t1926, R5)
    except:
        t2078 = None
    if t2078 == O:
        return True, f'beb8660c - t2078'
    try:
        t2079 = fork(add, t1391, t1927)
    except:
        t2079 = None
    try:
        t2080 = fill(I, t782, t1929)
    except:
        t2080 = None
    try:
        t2081 = size_f(t1930)
    except:
        t2081 = None
    try:
        t2082 = insert(t1186, t1931)
    except:
        t2082 = None
    try:
        t2083 = merge_f(t1932)
    except:
        t2083 = None
    try:
        t2084 = get_arg_rank_f(t985, size, F0)
    except:
        t2084 = None
    try:
        t2085 = vconcat(t1190, t1934)
    except:
        t2085 = None
    if t2085 == O:
        return True, f'1bfc4729 - t2085'
    try:
        t2086 = chain(palette_t, trim, t55)
    except:
        t2086 = None
    try:
        t2087 = chain(t1936, corners, outbox)
    except:
        t2087 = None
    try:
        t2088 = col_row(t1937, R1)
    except:
        t2088 = None
    try:
        t2089 = compose(size, t1938)
    except:
        t2089 = None
    try:
        t2090 = divide(t1771, t1939)
    except:
        t2090 = None
    try:
        t2091 = fill(t995, t300, t1940)
    except:
        t2091 = None
    try:
        t2092 = fork(recolor_o, color, t1941)
    except:
        t2092 = None
    try:
        t2093 = compose(t721, t23)
    except:
        t2093 = None
    try:
        t2094 = matcher(t1943, UNITY)
    except:
        t2094 = None
    try:
        t2095 = fork(connect, t713, t1210)
    except:
        t2095 = None
    try:
        t2096 = toindices(t1944)
    except:
        t2096 = None
    try:
        t2097 = f_ofcolor(t1946, BLACK)
    except:
        t2097 = None
    try:
        t2098 = fill(t1005, t246, t1947)
    except:
        t2098 = None
    if t2098 == O:
        return True, f'd4f3cd78 - t2098'
    try:
        t2099 = shift(t1948, UNITY)
    except:
        t2099 = None
    try:
        t2100 = compose(t1949, t1603)
    except:
        t2100 = None
    try:
        t2101 = chain(t10, t1419, t1950)
    except:
        t2101 = None
    try:
        t2102 = corner(t1422, R0)
    except:
        t2102 = None
    try:
        t2103 = fill(t48, t246, t1953)
    except:
        t2103 = None
    if t2103 == O:
        return True, f'dae9d2b5 - t2103'
    try:
        t2104 = rbind(vsplit, t47)
    except:
        t2104 = None
    try:
        t2105 = chain(t232, ineighbors, t23)
    except:
        t2105 = None
    try:
        t2106 = fill(I, t246, t1955)
    except:
        t2106 = None
    try:
        t2107 = o_g(t1956, R7)
    except:
        t2107 = None
    try:
        t2108 = mapply(box, t1957)
    except:
        t2108 = None
    try:
        t2109 = apply(t93, t9)
    except:
        t2109 = None
    try:
        t2110 = vperiod(t1960)
    except:
        t2110 = None
    try:
        t2111 = fill(t1224, t246, t1961)
    except:
        t2111 = None
    if t2111 == O:
        return True, f'bdad9b1f - t2111'
    try:
        t2112 = interval(t1962, TEN, FOUR)
    except:
        t2112 = None
    try:
        t2113 = sfilter_t(t1963, t1017)
    except:
        t2113 = None
    try:
        t2114 = lbind(greater, CYAN)
    except:
        t2114 = None
    try:
        t2115 = mapply(t1796, t7)
    except:
        t2115 = None
    try:
        t2116 = power(outbox, TWO)
    except:
        t2116 = None
    try:
        t2117 = fill(t259, t246, t1965)
    except:
        t2117 = None
    if t2117 == O:
        return True, f'99b1bc43 - t2117'
    try:
        t2118 = upscale_t(t1228, t1966)
    except:
        t2118 = None
    try:
        t2119 = center(t1967)
    except:
        t2119 = None
    try:
        t2120 = difference(t1968, t1801)
    except:
        t2120 = None
    try:
        t2121 = fill(t441, t246, t1970)
    except:
        t2121 = None
    if t2121 == O:
        return True, f'c3e719e8 - t2121'
    try:
        t2122 = index(I, t1233)
    except:
        t2122 = None
    try:
        t2123 = t1971(t1440)
    except:
        t2123 = None
    try:
        t2124 = height_f(t1972)
    except:
        t2124 = None
    try:
        t2125 = chain(t10, t1444, t1974)
    except:
        t2125 = None
    try:
        t2126 = fill(t275, t2, t1975)
    except:
        t2126 = None
    if t2126 == O:
        return True, f'6cdd2623 - t2126'
    try:
        t2127 = chain(t170, t1626, normalize)
    except:
        t2127 = None
    try:
        t2128 = mapply(t1628, t1976)
    except:
        t2128 = None
    try:
        t2129 = rbind(sfilter, t1978)
    except:
        t2129 = None
    try:
        t2130 = shoot(t1980, RIGHT)
    except:
        t2130 = None
    try:
        t2131 = subgrid(t1981, t3)
    except:
        t2131 = None
    try:
        t2132 = corner(t638, R1)
    except:
        t2132 = None
    try:
        t2133 = remove_t(t639, t1984)
    except:
        t2133 = None
    try:
        t2134 = colorfilter(t7, t251)
    except:
        t2134 = None
    try:
        t2135 = compose(t1985, color)
    except:
        t2135 = None
    try:
        t2136 = rbind(toobject, t643)
    except:
        t2136 = None
    try:
        t2137 = compose(t1821, t298)
    except:
        t2137 = None
    try:
        t2138 = fill(t1260, t264, t1988)
    except:
        t2138 = None
    try:
        t2139 = width_t(t1989)
    except:
        t2139 = None
    try:
        t2140 = decrement(t1990)
    except:
        t2140 = None
    try:
        t2141 = rbind(subtract, t1991)
    except:
        t2141 = None
    try:
        t2142 = sfilter_f(t12, t1992)
    except:
        t2142 = None
    try:
        t2143 = fill(t1470, t1826, t1994)
    except:
        t2143 = None
    if t2143 == O:
        return True, f'b548a754 - t2143'
    try:
        t2144 = paint(t855, t1995)
    except:
        t2144 = None
    try:
        t2145 = t1996(t42)
    except:
        t2145 = None
    try:
        t2146 = rbind(subtract, t1997)
    except:
        t2146 = None
    try:
        t2147 = color(t1998)
    except:
        t2147 = None
    try:
        t2148 = fork(hmatching, t10, t23)
    except:
        t2148 = None
    try:
        t2149 = apply(increment, t1999)
    except:
        t2149 = None
    try:
        t2150 = equality(t1275, t2000)
    except:
        t2150 = None
    try:
        t2151 = mapply(t1833, t6)
    except:
        t2151 = None
    try:
        t2152 = interval(ZERO, t1655, THREE)
    except:
        t2152 = None
    try:
        t2153 = rbind(t193, centerofmass)
    except:
        t2153 = None
    try:
        t2154 = fill(t1067, t246, t2003)
    except:
        t2154 = None
    try:
        t2155 = branch(t2004, TWO_BY_TWO, ZERO_BY_TWO)
    except:
        t2155 = None
    try:
        t2156 = f_ofcolor(t2005, BLACK)
    except:
        t2156 = None
    try:
        t2157 = equality(t2006, BLACK)
    except:
        t2157 = None
    try:
        t2158 = apply(t1842, t2007)
    except:
        t2158 = None
    try:
        t2159 = subtract(t1076, t1843)
    except:
        t2159 = None
    if t2117 == O:
        return True, f'31d5ba1a - t2117'
    try:
        t2160 = merge_t(t2009)
    except:
        t2160 = None
    if t2160 == O:
        return True, f'ff28f65a - t2160'
    try:
        t2161 = occurrences(t885, t1847)
    except:
        t2161 = None
    try:
        t2162 = corners(t2011)
    except:
        t2162 = None
    try:
        t2163 = compose(t1849, t1084)
    except:
        t2163 = None
    try:
        t2164 = astuple(t788, t1089)
    except:
        t2164 = None
    try:
        t2165 = fill(t1505, t1853, t2014)
    except:
        t2165 = None
    try:
        t2166 = fork(difference, t1506, t2015)
    except:
        t2166 = None
    try:
        t2167 = pair(t1855, t2016)
    except:
        t2167 = None
    try:
        t2168 = invert(t87)
    except:
        t2168 = None
    try:
        t2169 = difference(t169, t2017)
    except:
        t2169 = None
    try:
        t2170 = f_ofcolor(t1688, t1861)
    except:
        t2170 = None
    try:
        t2171 = compose(flip, t2021)
    except:
        t2171 = None
    try:
        t2172 = get_nth_f(t2022, F0)
    except:
        t2172 = None
    try:
        t2173 = sfilter_f(t181, t2023)
    except:
        t2173 = None
    try:
        t2174 = papply(pair, t1866, t2026)
    except:
        t2174 = None
    try:
        t2175 = fork(extract, t1323, t2027)
    except:
        t2175 = None
    try:
        t2176 = paint(I, t2028)
    except:
        t2176 = None
    if t2176 == O:
        return True, f'd43fd935 - t2176'
    try:
        t2177 = hconcat(t1325, t2029)
    except:
        t2177 = None
    try:
        t2178 = get_arg_rank_f(t1523, t2030, F0)
    except:
        t2178 = None
    try:
        t2179 = papply(pair, t1872, t2031)
    except:
        t2179 = None
    try:
        t2180 = mapply(t1873, t12)
    except:
        t2180 = None
    try:
        t2181 = combine_f(t1333, t2033)
    except:
        t2181 = None
    try:
        t2182 = fork(rapply, t2034, identity)
    except:
        t2182 = None
    try:
        t2183 = shape_f(t181)
    except:
        t2183 = None
    try:
        t2184 = subtract(NINE, t68)
    except:
        t2184 = None
    try:
        t2185 = corner(t1338, R2)
    except:
        t2185 = None
    try:
        t2186 = mapply(t353, t2040)
    except:
        t2186 = None
    try:
        t2187 = paint(I, t2041)
    except:
        t2187 = None
    if t2187 == O:
        return True, f'88a10436 - t2187'
    try:
        t2188 = rbind(vmatching, t187)
    except:
        t2188 = None
    try:
        t2189 = rbind(t1888, t2044)
    except:
        t2189 = None
    try:
        t2190 = rbind(colorcount_f, t1349)
    except:
        t2190 = None
    try:
        t2191 = combine(t1719, t2047)
    except:
        t2191 = None
    try:
        t2192 = branch(t2048, UNITY, TWO_BY_TWO)
    except:
        t2192 = None
    try:
        t2193 = hperiod(t1721)
    except:
        t2193 = None
    if t2121 == O:
        return True, f'27f8ce4f - t2121'
    try:
        t2194 = lbind(recolor_i, BLACK)
    except:
        t2194 = None
    try:
        t2195 = mapply(t1722, t2050)
    except:
        t2195 = None
    try:
        t2196 = height_f(t6)
    except:
        t2196 = None
    try:
        t2197 = lbind(shift, t2052)
    except:
        t2197 = None
    try:
        t2198 = replace(t2053, BLACK, BLUE)
    except:
        t2198 = None
    if t2198 == O:
        return True, f'e8593010 - t2198'
    try:
        t2199 = tophalf(t148)
    except:
        t2199 = None
    try:
        t2200 = subtract(t74, FOUR)
    except:
        t2200 = None
    try:
        t2201 = fork(shift, t1901, t298)
    except:
        t2201 = None
    try:
        t2202 = lbind(t2057, size)
    except:
        t2202 = None
    try:
        t2203 = combine(t1552, t2058)
    except:
        t2203 = None
    try:
        t2204 = merge_t(t2059)
    except:
        t2204 = None
    try:
        t2205 = branch(t1365, t2060, t1906)
    except:
        t2205 = None
    try:
        t2206 = compose(t10, toindices)
    except:
        t2206 = None
    try:
        t2207 = mfilter_f(t2061, vline_i)
    except:
        t2207 = None
    try:
        t2208 = fill(I, t246, t2063)
    except:
        t2208 = None
    if t2208 == O:
        return True, f'3eda0437 - t2208'
    try:
        t2209 = apply(color, t209)
    except:
        t2209 = None
    try:
        t2210 = difference(t957, t1162)
    except:
        t2210 = None
    try:
        t2211 = mir_rot_t(t2065, R3)
    except:
        t2211 = None
    if t2211 == O:
        return True, f'b8825c91 - t2211'
    try:
        t2212 = fill(t959, t246, t2066)
    except:
        t2212 = None
    if t2212 == O:
        return True, f'd90796e8 - t2212'
    try:
        t2213 = replace(t2067, NEG_ONE, BLACK)
    except:
        t2213 = None
    if t2213 == O:
        return True, f'af902bf9 - t2213'
    try:
        t2214 = lbind(greater, t2068)
    except:
        t2214 = None
    try:
        t2215 = paint(t1918, t2069)
    except:
        t2215 = None
    if t2215 == O:
        return True, f'05269061 - t2215'
    try:
        t2216 = merge_f(t2070)
    except:
        t2216 = None
    try:
        t2217 = astuple(ONE, t2072)
    except:
        t2217 = None
    try:
        t2218 = fill(t52, FOUR, t2073)
    except:
        t2218 = None
    try:
        t2219 = combine_f(t1922, t2074)
    except:
        t2219 = None
    try:
        t2220 = t973(t2075)
    except:
        t2220 = None
    if t2220 == O:
        return True, f'746b3537 - t2220'
    if t2117 == O:
        return True, f'3428a4f5 - t2117'
    try:
        t2221 = position(t393, t1924)
    except:
        t2221 = None
    try:
        t2222 = t1178(ONE)
    except:
        t2222 = None
    try:
        t2223 = lbind(t193, t219)
    except:
        t2223 = None
    try:
        t2224 = remove_f(t1929, t880)
    except:
        t2224 = None
    try:
        t2225 = greater(t1762, t2081)
    except:
        t2225 = None
    try:
        t2226 = rbind(contained, t2082)
    except:
        t2226 = None
    try:
        t2227 = product(t2083, t2083)
    except:
        t2227 = None
    try:
        t2228 = t435(t2084)
    except:
        t2228 = None
    try:
        t2229 = compose(t672, t2086)
    except:
        t2229 = None
    try:
        t2230 = apply(t1935, t1012)
    except:
        t2230 = None
    try:
        t2231 = fork(difference, t2087, outbox)
    except:
        t2231 = None
    try:
        t2232 = equality(t2088, BLACK)
    except:
        t2232 = None
    try:
        t2233 = get_arg_rank_f(t1770, t2089, F0)
    except:
        t2233 = None
    try:
        t2234 = upscale_f(t994, t2090)
    except:
        t2234 = None
    try:
        t2235 = mapply(t1942, t73)
    except:
        t2235 = None
    try:
        t2236 = fork(connect, t1774, t2093)
    except:
        t2236 = None
    try:
        t2237 = chain(t1594, double, t2094)
    except:
        t2237 = None
    try:
        t2238 = trim(t159)
    except:
        t2238 = None
    try:
        t2239 = fork(combine, t921, t2095)
    except:
        t2239 = None
    try:
        t2240 = index(t1595, ORIGIN)
    except:
        t2240 = None
    try:
        t2241 = rbind(manhattan, t91)
    except:
        t2241 = None
    try:
        t2242 = compose(t1945, t10)
    except:
        t2242 = None
    try:
        t2243 = fill(t1599, BLACK, t2097)
    except:
        t2243 = None
    if t2243 == O:
        return True, f'7c008303 - t2243'
    try:
        t2244 = mapply(t470, t2099)
    except:
        t2244 = None
    try:
        t2245 = fork(subtract, t1783, t2100)
    except:
        t2245 = None
    try:
        t2246 = fork(astuple, t2101, identity)
    except:
        t2246 = None
    try:
        t2247 = matcher(t10, THREE)
    except:
        t2247 = None
    try:
        t2248 = corner(t1952, R0)
    except:
        t2248 = None
    try:
        t2249 = compose(t1954, t2104)
    except:
        t2249 = None
    try:
        t2250 = chain(t1424, t1607, t2105)
    except:
        t2250 = None
    try:
        t2251 = shift(t2108, t248)
    except:
        t2251 = None
    try:
        t2252 = t1958(t2109)
    except:
        t2252 = None
    try:
        t2253 = hsplit(I, TWO)
    except:
        t2253 = None
    try:
        t2254 = apply(tojvec, t2112)
    except:
        t2254 = None
    try:
        t2255 = merge(t2113)
    except:
        t2255 = None
    try:
        t2256 = compose(t2114, size)
    except:
        t2256 = None
    try:
        t2257 = fill(I, t2, t2115)
    except:
        t2257 = None
    try:
        t2258 = chain(t1797, t232, t2116)
    except:
        t2258 = None
    try:
        t2259 = f_ofcolor(t1615, BLACK)
    except:
        t2259 = None
    try:
        t2260 = o_g(t436, R7)
    except:
        t2260 = None
    try:
        t2261 = fill(t1436, BLACK, t2120)
    except:
        t2261 = None
    if t2261 == O:
        return True, f'93b581b8 - t2261'
    try:
        t2262 = astuple(t2122, ORIGIN)
    except:
        t2262 = None
    try:
        t2263 = fill(t1807, t2, t2123)
    except:
        t2263 = None
    try:
        t2264 = increment(t2124)
    except:
        t2264 = None
    try:
        t2265 = fork(astuple, t2125, identity)
    except:
        t2265 = None
    try:
        t2266 = fork(apply, t1811, t2127)
    except:
        t2266 = None
    try:
        t2267 = fill(t449, t246, t2128)
    except:
        t2267 = None
    if t2267 == O:
        return True, f'6c434453 - t2267'
    try:
        t2268 = chain(t117, t1977, t1331)
    except:
        t2268 = None
    try:
        t2269 = compose(t1455, t2129)
    except:
        t2269 = None
    try:
        t2270 = fill(t1457, t264, t2130)
    except:
        t2270 = None
    if t2270 == O:
        return True, f'3bd67248 - t2270'
    try:
        t2271 = mir_rot_t(t2131, R2)
    except:
        t2271 = None
    if t2271 == O:
        return True, f'cd3c21df - t2271'
    try:
        t2272 = shoot(t2132, UP_RIGHT)
    except:
        t2272 = None
    try:
        t2273 = underfill(I, t246, t2133)
    except:
        t2273 = None
    if t2273 == O:
        return True, f'2281f1f4 - t2273'
    try:
        t2274 = sfilter_f(t125, t2135)
    except:
        t2274 = None
    try:
        t2275 = c_iz_n(S, t1, t400)
    except:
        t2275 = None
    try:
        t2276 = chain(t1987, t2136, neighbors)
    except:
        t2276 = None
    try:
        t2277 = chain(t460, t21, t2137)
    except:
        t2277 = None
    try:
        t2278 = astuple(ONE, t2139)
    except:
        t2278 = None
    try:
        t2279 = width_t(t1823)
    except:
        t2279 = None
    try:
        t2280 = compose(t1824, t2141)
    except:
        t2280 = None
    try:
        t2281 = difference(t12, t2142)
    except:
        t2281 = None
    try:
        t2282 = fork(either, t1480, t2148)
    except:
        t2282 = None
    try:
        t2283 = apply(tojvec, t2149)
    except:
        t2283 = None
    try:
        t2284 = underfill(I, RED, t2151)
    except:
        t2284 = None
    try:
        t2285 = rbind(contained, t2152)
    except:
        t2285 = None
    try:
        t2286 = rbind(mir_rot_f, R0)
    except:
        t2286 = None
    try:
        t2287 = connect(t1658, t2155)
    except:
        t2287 = None
    try:
        t2288 = fill(t873, BLACK, t2156)
    except:
        t2288 = None
    if t2288 == O:
        return True, f'b190f7f5 - t2288'
    try:
        t2289 = branch(t2157, width_f, height_f)
    except:
        t2289 = None
    try:
        t2290 = hconcat(t1662, t2158)
    except:
        t2290 = None
    try:
        t2291 = connect(t2008, t2159)
    except:
        t2291 = None
    try:
        t2292 = mapply(t2010, t2161)
    except:
        t2292 = None
    try:
        t2293 = apply(t1673, t2162)
    except:
        t2293 = None
    try:
        t2294 = fork(recolor_i, color, t2163)
    except:
        t2294 = None
    try:
        t2295 = get_rank(t2164, L1)
    except:
        t2295 = None
    try:
        t2296 = paint(t690, t2167)
    except:
        t2296 = None
    try:
        t2297 = astuple(THREE, t2168)
    except:
        t2297 = None
    try:
        t2298 = corner(t114, R0)
    except:
        t2298 = None
    try:
        t2299 = rbind(sfilter, t2171)
    except:
        t2299 = None
    try:
        t2300 = greater(t2172, SEVEN)
    except:
        t2300 = None
    try:
        t2301 = mapply(t702, t2173)
    except:
        t2301 = None
    try:
        t2302 = apply(t175, t2174)
    except:
        t2302 = None
    try:
        t2303 = fork(insert, t2175, t1868)
    except:
        t2303 = None
    try:
        t2304 = hsplit(t2177, THREE)
    except:
        t2304 = None
    try:
        t2305 = underfill(I, t246, t2178)
    except:
        t2305 = None
    if t2305 == O:
        return True, f'1b60fb0c - t2305'
    try:
        t2306 = apply(t175, t2179)
    except:
        t2306 = None
    try:
        t2307 = fill(I, t246, t2180)
    except:
        t2307 = None
    if t2307 == O:
        return True, f'fcc82909 - t2307'
    try:
        t2308 = paint(t437, t2181)
    except:
        t2308 = None
    if t2308 == O:
        return True, f'a61f2674 - t2308'
    try:
        t2309 = compose(t10, t2182)
    except:
        t2309 = None
    try:
        t2310 = fill(t1706, t264, t599)
    except:
        t2310 = None
    if t2310 == O:
        return True, f'ea32f347 - t2310'
    try:
        t2311 = interval(ZERO, t2184, ONE)
    except:
        t2311 = None
    try:
        t2312 = shoot(t2185, DOWN_LEFT)
    except:
        t2312 = None
    try:
        t2313 = prapply(multiply, t2039, t1012)
    except:
        t2313 = None
    try:
        t2314 = fill(t71, t2, t2186)
    except:
        t2314 = None
    if t2314 == O:
        return True, f'bc1d5164 - t2314'
    try:
        t2315 = rbind(greater, t929)
    except:
        t2315 = None
    try:
        t2316 = paint(t934, t2191)
    except:
        t2316 = None
    try:
        t2317 = branch(t1720, RIGHT, t2192)
    except:
        t2317 = None
    try:
        t2318 = astuple(t2049, t2193)
    except:
        t2318 = None
    try:
        t2319 = compose(t2194, outbox)
    except:
        t2319 = None
    try:
        t2320 = paint(t1354, t2195)
    except:
        t2320 = None
    if t2320 == O:
        return True, f'321b1fc6 - t2320'
    try:
        t2321 = toivec(t2196)
    except:
        t2321 = None
    try:
        t2322 = t738(t2199)
    except:
        t2322 = None
    try:
        t2323 = power(t1898, t2200)
    except:
        t2323 = None
    try:
        t2324 = fork(intersection, toindices, t2201)
    except:
        t2324 = None
    try:
        t2325 = lbind(rbind, intersection)
    except:
        t2325 = None
    try:
        t2326 = apply(t745, t2203)
    except:
        t2326 = None
    try:
        t2327 = mir_rot_t(t2204, R6)
    except:
        t2327 = None
    try:
        t2328 = fill(t71, t246, t2205)
    except:
        t2328 = None
    if t2328 == O:
        return True, f'794b24be - t2328'
    try:
        t2329 = get_nth_f(t1556, F0)
    except:
        t2329 = None
    try:
        t2330 = size_f(t2207)
    except:
        t2330 = None
    try:
        t2331 = t1157(t1210)
    except:
        t2331 = None
    if t2271 == O:
        return True, f'ce602527 - t2271'
    try:
        t2332 = other_f(t2209, t2064)
    except:
        t2332 = None
    try:
        t2333 = merge_f(t2210)
    except:
        t2333 = None
    try:
        t2334 = recolor_o(t246, t2216)
    except:
        t2334 = None
    try:
        t2335 = canvas(BLACK, t2217)
    except:
        t2335 = None
    try:
        t2336 = merge(t389)
    except:
        t2336 = None
    try:
        t2337 = underfill(I, t246, t2219)
    except:
        t2337 = None
    if t2337 == O:
        return True, f'd4a91cb9 - t2337'
    try:
        t2338 = lbind(multiply, t2221)
    except:
        t2338 = None
    try:
        t2339 = fork(shift, identity, t2222)
    except:
        t2339 = None
    try:
        t2340 = compose(t342, t398)
    except:
        t2340 = None
    try:
        t2341 = lbind(vmatching, t1929)
    except:
        t2341 = None
    try:
        t2342 = branch(t2225, t1930, t1581)
    except:
        t2342 = None
    try:
        t2343 = fill(t1584, t264, t2228)
    except:
        t2343 = None
    if t2343 == O:
        return True, f'694f12f3 - t2343'
    try:
        t2344 = mfilter_f(t7, t2229)
    except:
        t2344 = None
    try:
        t2345 = mapply(t386, t2230)
    except:
        t2345 = None
    try:
        t2346 = chain(t1400, t1768, t2231)
    except:
        t2346 = None
    try:
        t2347 = fill(t406, t585, t2233)
    except:
        t2347 = None
    if t2347 == O:
        return True, f'3345333e - t2347'
    try:
        t2348 = corner(t1588, R0)
    except:
        t2348 = None
    try:
        t2349 = mapply(corners, t957)
    except:
        t2349 = None
    try:
        t2350 = mapply(t2092, t354)
    except:
        t2350 = None
    try:
        t2351 = underfill(t588, CYAN, t2235)
    except:
        t2351 = None
    try:
        t2352 = fork(recolor_i, t143, t2236)
    except:
        t2352 = None
    try:
        t2353 = fork(add, t1407, t2237)
    except:
        t2353 = None
    try:
        t2354 = t1777(t2238)
    except:
        t2354 = None
    try:
        t2355 = o_g(t1001, R3)
    except:
        t2355 = None
    try:
        t2356 = replace(t1595, t251, t2240)
    except:
        t2356 = None
    try:
        t2357 = chain(even, t2241, initset)
    except:
        t2357 = None
    try:
        t2358 = rbind(sfilter, t2242)
    except:
        t2358 = None
    try:
        t2359 = fill(t802, RED, t2244)
    except:
        t2359 = None
    try:
        t2360 = get_arg_rank_f(t12, t2245, F0)
    except:
        t2360 = None
    try:
        t2361 = normalize_o(t241)
    except:
        t2361 = None
    try:
        t2362 = compose(flip, t2247)
    except:
        t2362 = None
    try:
        t2363 = subtract(t2102, t2248)
    except:
        t2363 = None
    try:
        t2364 = t2249(I)
    except:
        t2364 = None
    try:
        t2365 = sfilter_f(t808, t2250)
    except:
        t2365 = None
    try:
        t2366 = order(t2107, t302)
    except:
        t2366 = None
    try:
        t2367 = fill(I, t2, t2251)
    except:
        t2367 = None
    if t2367 == O:
        return True, f'5c2c9af4 - t2367'
    try:
        t2368 = fill(t812, t246, t2252)
    except:
        t2368 = None
    if t2368 == O:
        return True, f'23581191 - t2368'
    try:
        t2369 = extract(t2253, t1014)
    except:
        t2369 = None
    try:
        t2370 = fill(t1793, GRAY, t2254)
    except:
        t2370 = None
    try:
        t2371 = mir_rot_t(t2255, R6)
    except:
        t2371 = None
    try:
        t2372 = mfilter_f(t1964, t2256)
    except:
        t2372 = None
    try:
        t2373 = mapply(delta, t7)
    except:
        t2373 = None
    try:
        t2374 = get_arg_rank_f(t1227, t2258, F0)
    except:
        t2374 = None
    try:
        t2375 = fill(t2118, BLACK, t2259)
    except:
        t2375 = None
    if t2375 == O:
        return True, f'77fdfe62 - t2375'
    try:
        t2376 = rbind(subgrid, t436)
    except:
        t2376 = None
    try:
        t2377 = initset(t2262)
    except:
        t2377 = None
    try:
        t2378 = power(t1028, THREE)
    except:
        t2378 = None
    try:
        t2379 = interval(ZERO, t1441, t2264)
    except:
        t2379 = None
    try:
        t2380 = fork(difference, box, corners)
    except:
        t2380 = None
    try:
        t2381 = fork(mapply, t113, t2266)
    except:
        t2381 = None
    try:
        t2382 = rbind(sfilter, t1814)
    except:
        t2382 = None
    try:
        t2383 = corner(t638, R0)
    except:
        t2383 = None
    try:
        t2384 = compose(t67, t1210)
    except:
        t2384 = None
    try:
        t2385 = mapply(t1637, t2274)
    except:
        t2385 = None
    try:
        t2386 = compose(t1639, t2276)
    except:
        t2386 = None
    try:
        t2387 = lbind(compose, size)
    except:
        t2387 = None
    try:
        t2388 = crop(t1989, ORIGIN, t2278)
    except:
        t2388 = None
    try:
        t2389 = astuple(t2140, t2279)
    except:
        t2389 = None
    try:
        t2390 = sfilter_f(t1644, t2280)
    except:
        t2390 = None
    try:
        t2391 = mapply(t1645, t2281)
    except:
        t2391 = None
    try:
        t2392 = t853(FOUR)
    except:
        t2392 = None
    try:
        t2393 = branch(t140, t342, t438)
    except:
        t2393 = None
    try:
        t2394 = chain(even, t2146, t23)
    except:
        t2394 = None
    try:
        t2395 = toindices(t1998)
    except:
        t2395 = None
    try:
        t2396 = sfilter_f(t1830, t2282)
    except:
        t2396 = None
    try:
        t2397 = prapply(shift, t1651, t2283)
    except:
        t2397 = None
    try:
        t2398 = branch(t2150, identity, t689)
    except:
        t2398 = None
    try:
        t2399 = chain(invert, t45, t863)
    except:
        t2399 = None
    try:
        t2400 = compose(t2285, t23)
    except:
        t2400 = None
    try:
        t2401 = rbind(greater, t264)
    except:
        t2401 = None
    try:
        t2402 = fill(t481, t264, t2287)
    except:
        t2402 = None
    if t2402 == O:
        return True, f'6e02f1e3 - t2402'
    try:
        t2403 = t2289(t1288)
    except:
        t2403 = None
    try:
        t2404 = t488(t2290)
    except:
        t2404 = None
    if t2404 == O:
        return True, f'4093f84a - t2404'
    try:
        t2405 = fill(I, GREEN, t2291)
    except:
        t2405 = None
    try:
        t2406 = mapply(neighbors, t6)
    except:
        t2406 = None
    try:
        t2407 = fill(t885, RED, t2292)
    except:
        t2407 = None
    try:
        t2408 = paint(t456, t2293)
    except:
        t2408 = None
    if t2408 == O:
        return True, f'952a094c - t2408'
    try:
        t2409 = mapply(t2294, t125)
    except:
        t2409 = None
    try:
        t2410 = astuple(t167, t2295)
    except:
        t2410 = None
    try:
        t2411 = shift(t6, DOWN_LEFT)
    except:
        t2411 = None
    try:
        t2412 = mapply(t2166, t9)
    except:
        t2412 = None
    try:
        t2413 = astuple(TWO, t2168)
    except:
        t2413 = None
    try:
        t2414 = initset(t50)
    except:
        t2414 = None
    try:
        t2415 = shift(t2170, t2298)
    except:
        t2415 = None
    try:
        t2416 = chain(t10, t1101, t2299)
    except:
        t2416 = None
    try:
        t2417 = greater(t2172, THREE)
    except:
        t2417 = None
    try:
        t2418 = fill(I, BLUE, t2301)
    except:
        t2418 = None
    if t2418 == O:
        return True, f'6cf79266 - t2418'
    try:
        t2419 = lbind(recolor_i, ZERO)
    except:
        t2419 = None
    try:
        t2420 = merge_t(t2304)
    except:
        t2420 = None
    try:
        t2421 = apply(t2032, t174)
    except:
        t2421 = None
    try:
        t2422 = compose(backdrop, t2309)
    except:
        t2422 = None
    try:
        t2423 = position(t181, t91)
    except:
        t2423 = None
    try:
        t2424 = apply(t2036, t2311)
    except:
        t2424 = None
    try:
        t2425 = shoot(t2185, UP_RIGHT)
    except:
        t2425 = None
    try:
        t2426 = mapply(t1122, t2313)
    except:
        t2426 = None
    try:
        t2427 = chain(t932, t2189, t342)
    except:
        t2427 = None
    try:
        t2428 = chain(t2190, t232, dneighbors)
    except:
        t2428 = None
    try:
        t2429 = sizefilter(t933, ONE)
    except:
        t2429 = None
    try:
        t2430 = mir_rot_t(t2316, R6)
    except:
        t2430 = None
    try:
        t2431 = t4(t2317)
    except:
        t2431 = None
    try:
        t2432 = lbind(multiply, t2318)
    except:
        t2432 = None
    try:
        t2433 = fork(combine, identity, t2319)
    except:
        t2433 = None
    try:
        t2434 = add(t2321, TWO_BY_ZERO)
    except:
        t2434 = None
    try:
        t2435 = compose(toivec, t302)
    except:
        t2435 = None
    try:
        t2436 = paint(t2054, t2322)
    except:
        t2436 = None
    if t2436 == O:
        return True, f'ea9794b1 - t2436'
    try:
        t2437 = even(t74)
    except:
        t2437 = None
    try:
        t2438 = partition(t1145)
    except:
        t2438 = None
    try:
        t2439 = chain(t2202, t2325, toindices)
    except:
        t2439 = None
    try:
        t2440 = rbind(interval, ONE)
    except:
        t2440 = None
    try:
        t2441 = astuple(t370, t1553)
    except:
        t2441 = None
    if t2436 == O:
        return True, f'75b8110e - t2436'
    try:
        t2442 = t2206(t2329)
    except:
        t2442 = None
    try:
        t2443 = mfilter_f(t2061, hline_i)
    except:
        t2443 = None
    try:
        t2444 = branch(t1912, t2064, t2332)
    except:
        t2444 = None
    try:
        t2445 = recolor_o(t264, t2333)
    except:
        t2445 = None
    try:
        t2446 = compose(t2214, t10)
    except:
        t2446 = None
    try:
        t2447 = fill(t1572, t264, t2334)
    except:
        t2447 = None
    if t2447 == O:
        return True, f'868de0fa - t2447'
    try:
        t2448 = hconcat(t1920, t2335)
    except:
        t2448 = None
    try:
        t2449 = paint(t2218, t2336)
    except:
        t2449 = None
    try:
        t2450 = t823(SEVEN)
    except:
        t2450 = None
    try:
        t2451 = fork(equality, t2340, t342)
    except:
        t2451 = None
    try:
        t2452 = sfilter_f(t2224, t2341)
    except:
        t2452 = None
    try:
        t2453 = fill(t1185, t246, t2342)
    except:
        t2453 = None
    try:
        t2454 = chain(flip, t2226, t298)
    except:
        t2454 = None
    try:
        t2455 = fill(t920, t264, t2344)
    except:
        t2455 = None
    try:
        t2456 = shape_f(t99)
    except:
        t2456 = None
    try:
        t2457 = mfilter_f(t1192, t2346)
    except:
        t2457 = None
    try:
        t2458 = branch(t2232, identity, t72)
    except:
        t2458 = None
    try:
        t2459 = shift(t2234, t2348)
    except:
        t2459 = None
    try:
        t2460 = fill(t2091, t246, t2349)
    except:
        t2460 = None
    if t2460 == O:
        return True, f'b6afb2da - t2460'
    try:
        t2461 = paint(I, t2350)
    except:
        t2461 = None
    if t2461 == O:
        return True, f'045e512c - t2461'
    try:
        t2462 = t1201(t2354, TWO)
    except:
        t2462 = None
    try:
        t2463 = mapply(t2239, t2355)
    except:
        t2463 = None
    try:
        t2464 = branch(t1002, righthalf, bottomhalf)
    except:
        t2464 = None
    try:
        t2465 = sfilter_f(t2096, t2357)
    except:
        t2465 = None
    try:
        t2466 = chain(t626, t2358, normalize)
    except:
        t2466 = None
    try:
        t2467 = difference(t1416, t1781)
    except:
        t2467 = None
    try:
        t2468 = normalize_o(t2360)
    except:
        t2468 = None
    try:
        t2469 = shift(t2361, UNITY)
    except:
        t2469 = None
    try:
        t2470 = sfilter_f(t1951, t2362)
    except:
        t2470 = None
    try:
        t2471 = move(I, t1952, t2363)
    except:
        t2471 = None
    try:
        t2472 = pair(t1215, t2364)
    except:
        t2472 = None
    try:
        t2473 = outbox(t2365)
    except:
        t2473 = None
    try:
        t2474 = t1788(TWO)
    except:
        t2474 = None
    try:
        t2475 = apply(color, t2366)
    except:
        t2475 = None
    try:
        t2476 = asobject(t2369)
    except:
        t2476 = None
    try:
        t2477 = get_color_rank_t(t2371, L1)
    except:
        t2477 = None
    try:
        t2478 = fill(I, RED, t2372)
    except:
        t2478 = None
    try:
        t2479 = fill(t2257, BLACK, t2373)
    except:
        t2479 = None
    if t2479 == O:
        return True, f'6e19193c - t2479'
    try:
        t2480 = corner(t2374, R0)
    except:
        t2480 = None
    try:
        t2481 = compose(t1434, t2376)
    except:
        t2481 = None
    try:
        t2482 = rbind(occurrences, t2377)
    except:
        t2482 = None
    try:
        t2483 = t2378(t1440)
    except:
        t2483 = None
    try:
        t2484 = rbind(contained, t2379)
    except:
        t2484 = None
    try:
        t2485 = asindices(t274)
    except:
        t2485 = None
    try:
        t2486 = fork(combine, t2269, t2382)
    except:
        t2486 = None
    try:
        t2487 = shoot(t2383, NEG_UNITY)
    except:
        t2487 = None
    try:
        t2488 = matcher(t2384, t251)
    except:
        t2488 = None
    try:
        t2489 = paint(t456, t2385)
    except:
        t2489 = None
    if t2489 == O:
        return True, f'1a07d186 - t2489'
    try:
        t2490 = sfilter_f(t26, t2386)
    except:
        t2490 = None
    try:
        t2491 = lbind(lbind, intersection)
    except:
        t2491 = None
    try:
        t2492 = vupscale(t2388, t2139)
    except:
        t2492 = None
    try:
        t2493 = crop(t1263, t1642, t2389)
    except:
        t2493 = None
    try:
        t2494 = combine(t1468, t2390)
    except:
        t2494 = None
    try:
        t2495 = paint(I, t2391)
    except:
        t2495 = None
    try:
        t2496 = fill(t1993, t246, t2392)
    except:
        t2496 = None
    if t2496 == O:
        return True, f'6e82a1ae - t2496'
    try:
        t2497 = t2393(t42)
    except:
        t2497 = None
    try:
        t2498 = sfilter_f(t1649, t2394)
    except:
        t2498 = None
    try:
        t2499 = matcher(t215, t2395)
    except:
        t2499 = None
    try:
        t2500 = mapply(t1274, t2396)
    except:
        t2500 = None
    try:
        t2501 = merge_f(t2397)
    except:
        t2501 = None
    try:
        t2502 = t2398(t473)
    except:
        t2502 = None
    try:
        t2503 = fork(shoot, identity, t2399)
    except:
        t2503 = None
    try:
        t2504 = sfilter_t(t2002, t2400)
    except:
        t2504 = None
    try:
        t2505 = compose(halve, width_f)
    except:
        t2505 = None
    try:
        t2506 = multiply(t1661, t2403)
    except:
        t2506 = None
    try:
        t2507 = fill(t1844, t246, t2406)
    except:
        t2507 = None
    if t2507 == O:
        return True, f'913fb3ed - t2507'
    try:
        t2508 = t1494(t190)
    except:
        t2508 = None
    try:
        t2509 = paint(t456, t2409)
    except:
        t2509 = None
    if t2509 == O:
        return True, f'd89b689b - t2509'
    try:
        t2510 = lbind(hmatching, t91)
    except:
        t2510 = None
    try:
        t2511 = get_rank(t2164, F0)
    except:
        t2511 = None
    try:
        t2512 = fill(t2165, t246, t2411)
    except:
        t2512 = None
    try:
        t2513 = fill(I, t246, t2412)
    except:
        t2513 = None
    if t2513 == O:
        return True, f'22233c11 - t2513'
    try:
        t2514 = compose(dedupe, totuple)
    except:
        t2514 = None
    try:
        t2515 = initset(t2413)
    except:
        t2515 = None
    try:
        t2516 = difference(t2169, t2414)
    except:
        t2516 = None
    try:
        t2517 = branch(t2417, FOUR, ZERO)
    except:
        t2517 = None
    try:
        t2518 = partition(t2302)
    except:
        t2518 = None
    try:
        t2519 = chain(t2419, delta, t2303)
    except:
        t2519 = None
    try:
        t2520 = partition(t2306)
    except:
        t2520 = None
    try:
        t2521 = multiply(t2183, t2423)
    except:
        t2521 = None
    try:
        t2522 = mapply(t1878, t2424)
    except:
        t2522 = None
    try:
        t2523 = combine(t2312, t2425)
    except:
        t2523 = None
    try:
        t2524 = paint(I, t2426)
    except:
        t2524 = None
    if t2524 == O:
        return True, f'1f0c79e5 - t2524'
    try:
        t2525 = compose(t2315, t302)
    except:
        t2525 = None
    try:
        t2526 = fork(recolor_i, color, t2427)
    except:
        t2526 = None
    try:
        t2527 = matcher(t2428, YELLOW)
    except:
        t2527 = None
    try:
        t2528 = merge_f(t2429)
    except:
        t2528 = None
    try:
        t2529 = contained(TWO_BY_TWO, t357)
    except:
        t2529 = None
    try:
        t2530 = fill(t71, t246, t2431)
    except:
        t2530 = None
    if t2530 == O:
        return True, f'd4469b4b - t2530'
    try:
        t2531 = chain(t170, t2433, t1309)
    except:
        t2531 = None
    try:
        t2532 = shift(t2051, t2434)
    except:
        t2532 = None
    try:
        t2533 = compose(t2197, t2435)
    except:
        t2533 = None
    try:
        t2534 = upscale_t(t75, FOUR)
    except:
        t2534 = None
    try:
        t2535 = fork(t193, t1732, t2439)
    except:
        t2535 = None
    try:
        t2536 = lbind(t2440, ZERO)
    except:
        t2536 = None
    try:
        t2537 = crop(t2327, ORIGIN, t2441)
    except:
        t2537 = None
    if t2537 == O:
        return True, f'a416b8f3 - t2537'
    try:
        t2538 = t2206(t1736)
    except:
        t2538 = None
    try:
        t2539 = size_f(t2443)
    except:
        t2539 = None
    try:
        t2540 = t1157(t298)
    except:
        t2540 = None
    try:
        t2541 = f_ofcolor(I, t1741)
    except:
        t2541 = None
    try:
        t2542 = paint(t1742, t2445)
    except:
        t2542 = None
    if t2542 == O:
        return True, f'83302e8f - t2542'
    if t2537 == O:
        return True, f'963e52fc - t2537'
    try:
        t2543 = sfilter_f(t26, t2446)
    except:
        t2543 = None
    try:
        t2544 = hsplit(t2448, TWO)
    except:
        t2544 = None
    try:
        t2545 = downscale(t2449, TWO)
    except:
        t2545 = None
    if t2545 == O:
        return True, f'36fdfd69 - t2545'
    try:
        t2546 = apply(t2338, t1012)
    except:
        t2546 = None
    try:
        t2547 = mapply(t2339, t2450)
    except:
        t2547 = None
    try:
        t2548 = compose(invert, t2451)
    except:
        t2548 = None
    try:
        t2549 = f_ofcolor(t2453, t246)
    except:
        t2549 = None
    try:
        t2550 = sfilter_f(t984, t2454)
    except:
        t2550 = None
    try:
        t2551 = fork(equality, t1044, t368)
    except:
        t2551 = None
    try:
        t2552 = add(DOWN, t2456)
    except:
        t2552 = None
    if t2489 == O:
        return True, f'd687bc17 - t2489'
    try:
        t2553 = fill(I, t246, t2457)
    except:
        t2553 = None
    if t2553 == O:
        return True, f'e73095fd - t2553'
    try:
        t2554 = chain(t582, t1401, t2458)
    except:
        t2554 = None
    try:
        t2555 = paint(t230, t2459)
    except:
        t2555 = None
    if t2555 == O:
        return True, f'8a004b2b - t2555'
    try:
        t2556 = add(t19, DOWN_LEFT)
    except:
        t2556 = None
    try:
        t2557 = matcher(t1943, DOWN)
    except:
        t2557 = None
    try:
        t2558 = apply(t234, t2462)
    except:
        t2558 = None
    try:
        t2559 = fill(t1001, t2, t2463)
    except:
        t2559 = None
    if t2559 == O:
        return True, f'0962bcdd - t2559'
    try:
        t2560 = t2464(I)
    except:
        t2560 = None
    try:
        t2561 = fill(I, t2, t2465)
    except:
        t2561 = None
    try:
        t2562 = colorfilter(t2467, RED)
    except:
        t2562 = None
    try:
        t2563 = lbind(shift, t2468)
    except:
        t2563 = None
    try:
        t2564 = toindices(t2469)
    except:
        t2564 = None
    try:
        t2565 = corner(t126, R0)
    except:
        t2565 = None
    try:
        t2566 = get_nth_f(t1213, L1)
    except:
        t2566 = None
    try:
        t2567 = backdrop(t2473)
    except:
        t2567 = None
    try:
        t2568 = fill(t2106, t300, t2474)
    except:
        t2568 = None
    try:
        t2569 = dedupe(t2475)
    except:
        t2569 = None
    try:
        t2570 = hperiod(t2476)
    except:
        t2570 = None
    try:
        t2571 = apply(t817, t1795)
    except:
        t2571 = None
    try:
        t2572 = shape_f(t2374)
    except:
        t2572 = None
    try:
        t2573 = extract(t2260, t2481)
    except:
        t2573 = None
    try:
        t2574 = compose(t2482, t442)
    except:
        t2574 = None
    try:
        t2575 = fill(t2263, t2, t2483)
    except:
        t2575 = None
    try:
        t2576 = t2380(t2485)
    except:
        t2576 = None
    try:
        t2577 = lbind(t193, t7)
    except:
        t2577 = None
    try:
        t2578 = chain(t626, t2486, normalize)
    except:
        t2578 = None
    try:
        t2579 = combine(t2272, t2487)
    except:
        t2579 = None
    try:
        t2580 = sfilter_f(t2134, t2488)
    except:
        t2580 = None
    try:
        t2581 = replace(t1986, t2275, t1853)
    except:
        t2581 = None
    try:
        t2582 = fill(t643, BLACK, t2490)
    except:
        t2582 = None
    if t2582 == O:
        return True, f'91714a58 - t2582'
    try:
        t2583 = compose(t2387, t2491)
    except:
        t2583 = None
    try:
        t2584 = apply(t713, t729)
    except:
        t2584 = None
    try:
        t2585 = hconcat(t1989, t2492)
    except:
        t2585 = None
    try:
        t2586 = repeat(t2493, BURGUNDY)
    except:
        t2586 = None
    try:
        t2587 = fill(t136, ONE, t2494)
    except:
        t2587 = None
    try:
        t2588 = lbind(rbind, add)
    except:
        t2588 = None
    try:
        t2589 = astuple(t2145, t2497)
    except:
        t2589 = None
    try:
        t2590 = fill(t1828, ORANGE, t2498)
    except:
        t2590 = None
    if t2590 == O:
        return True, f'db3e9e38 - t2590'
    try:
        t2591 = mfilter_f(t7, t2499)
    except:
        t2591 = None
    try:
        t2592 = paint(I, t2500)
    except:
        t2592 = None
    if t2592 == O:
        return True, f'cbded52d - t2592'
    try:
        t2593 = fill(t861, t246, t2501)
    except:
        t2593 = None
    if t2593 == O:
        return True, f'97999447 - t2593'
    try:
        t2594 = normalize(t2502)
    except:
        t2594 = None
    try:
        t2595 = mapply(t10, t2504)
    except:
        t2595 = None
    try:
        t2596 = compose(t2401, t2505)
    except:
        t2596 = None
    try:
        t2597 = crement(t2506)
    except:
        t2597 = None
    try:
        t2598 = paint(t2405, t187)
    except:
        t2598 = None
    try:
        t2599 = fill(t1845, t300, t2508)
    except:
        t2599 = None
    try:
        t2600 = lbind(vmatching, t91)
    except:
        t2600 = None
    try:
        t2601 = astuple(t167, t2511)
    except:
        t2601 = None
    try:
        t2602 = chain(t897, size, t2514)
    except:
        t2602 = None
    try:
        t2603 = insert(t2297, t2515)
    except:
        t2603 = None
    try:
        t2604 = get_nth_f(t2516, F0)
    except:
        t2604 = None
    try:
        t2605 = initset(identity)
    except:
        t2605 = None
    try:
        t2606 = f_ofcolor(I, t1861)
    except:
        t2606 = None
    try:
        t2607 = compose(t298, t2299)
    except:
        t2607 = None
    try:
        t2608 = branch(t2300, EIGHT, t2517)
    except:
        t2608 = None
    try:
        t2609 = sizefilter(t2518, FOUR)
    except:
        t2609 = None
    try:
        t2610 = fork(combine, t2303, t2519)
    except:
        t2610 = None
    try:
        t2611 = crop(t2420, ORIGIN, t1582)
    except:
        t2611 = None
    try:
        t2612 = sizefilter(t2520, FOUR)
    except:
        t2612 = None
    try:
        t2613 = compose(decrement, t721)
    except:
        t2613 = None
    try:
        t2614 = mapply(t2422, t17)
    except:
        t2614 = None
    try:
        t2615 = apply(t2035, t2521)
    except:
        t2615 = None
    try:
        t2616 = paint(t1120, t2522)
    except:
        t2616 = None
    try:
        t2617 = combine(t2038, t2523)
    except:
        t2617 = None
    try:
        t2618 = fork(both, t2188, t2525)
    except:
        t2618 = None
    try:
        t2619 = mapply(t2526, t1348)
    except:
        t2619 = None
    try:
        t2620 = extract(t2045, t2527)
    except:
        t2620 = None
    try:
        t2621 = fill(t2046, t246, t2528)
    except:
        t2621 = None
    if t2621 == O:
        return True, f'c0f76784 - t2621'
    try:
        t2622 = mir_rot_t(t2316, R5)
    except:
        t2622 = None
    try:
        t2623 = fork(apply, t1893, t2531)
    except:
        t2623 = None
    try:
        t2624 = fill(t1723, RED, t2532)
    except:
        t2624 = None
    try:
        t2625 = fork(recolor_o, t937, t2533)
    except:
        t2625 = None
    try:
        t2626 = astuple(TWO, TWO)
    except:
        t2626 = None
    try:
        t2627 = compose(t23, t2535)
    except:
        t2627 = None
    try:
        t2628 = connect(t2442, t2538)
    except:
        t2628 = None
    try:
        t2629 = greater(t2330, t2539)
    except:
        t2629 = None
    try:
        t2630 = hconcat(t2331, t2540)
    except:
        t2630 = None
    try:
        t2631 = col_row(t564, R2)
    except:
        t2631 = None
    try:
        t2632 = get_nth_t(t2544, F0)
    except:
        t2632 = None
    try:
        t2633 = mapply(t2076, t2546)
    except:
        t2633 = None
    try:
        t2634 = paint(t2077, t2547)
    except:
        t2634 = None
    if t2634 == O:
        return True, f'ae3edfdc - t2634'
    try:
        t2635 = chain(initset, t2223, t1950)
    except:
        t2635 = None
    try:
        t2636 = get_arg_rank_f(t2452, t302, L1)
    except:
        t2636 = None
    try:
        t2637 = merge_f(t2550)
    except:
        t2637 = None
    try:
        t2638 = sfilter_f(t2227, t2551)
    except:
        t2638 = None
    try:
        t2639 = fork(add, height_f, width_f)
    except:
        t2639 = None
    try:
        t2640 = decrement(t2552)
    except:
        t2640 = None
    try:
        t2641 = t2458(t1769)
    except:
        t2641 = None
    try:
        t2642 = fork(subtract, t65, t1949)
    except:
        t2642 = None
    try:
        t2643 = initset(t2556)
    except:
        t2643 = None
    try:
        t2644 = compose(t567, t2557)
    except:
        t2644 = None
    try:
        t2645 = get_nth_t(t2558, L1)
    except:
        t2645 = None
    try:
        t2646 = shape_t(t2560)
    except:
        t2646 = None
    try:
        t2647 = difference(t2096, t2465)
    except:
        t2647 = None
    try:
        t2648 = chain(t170, t2358, normalize)
    except:
        t2648 = None
    try:
        t2649 = mapply(toindices, t2562)
    except:
        t2649 = None
    try:
        t2650 = apply(t2246, t2564)
    except:
        t2650 = None
    try:
        t2651 = shape_f(t126)
    except:
        t2651 = None
    try:
        t2652 = t602(t2566)
    except:
        t2652 = None
    try:
        t2653 = sfilter_t(t2472, t23)
    except:
        t2653 = None
    try:
        t2654 = gravitate(t2567, t604)
    except:
        t2654 = None
    try:
        t2655 = size_t(t2569)
    except:
        t2655 = None
    try:
        t2656 = astuple(t2110, t2570)
    except:
        t2656 = None
    try:
        t2657 = f_ofcolor(t2371, t2477)
    except:
        t2657 = None
    try:
        t2658 = intersection(t2372, t2571)
    except:
        t2658 = None
    try:
        t2659 = subtract(t2480, t2572)
    except:
        t2659 = None
    try:
        t2660 = center(t2573)
    except:
        t2660 = None
    try:
        t2661 = compose(t1361, t2574)
    except:
        t2661 = None
    try:
        t2662 = chain(flip, t2484, t23)
    except:
        t2662 = None
    try:
        t2663 = apply(t2265, t2576)
    except:
        t2663 = None
    try:
        t2664 = astuple(t15, t105)
    except:
        t2664 = None
    try:
        t2665 = compose(positive, size)
    except:
        t2665 = None
    try:
        t2666 = combine(t1983, t2579)
    except:
        t2666 = None
    try:
        t2667 = apply(t1210, t2580)
    except:
        t2667 = None
    try:
        t2668 = c_iz_n(S, t1, t138)
    except:
        t2668 = None
    try:
        t2669 = fork(t36, t2277, t2583)
    except:
        t2669 = None
    try:
        t2670 = fill(t2138, t300, t2584)
    except:
        t2670 = None
    try:
        t2671 = mir_rot_t(t2492, R1)
    except:
        t2671 = None
    try:
        t2672 = merge(t2586)
    except:
        t2672 = None
    try:
        t2673 = o_g(t2587, R5)
    except:
        t2673 = None
    try:
        t2674 = apply(t1210, t1827)
    except:
        t2674 = None
    try:
        t2675 = other_f(t42, t2589)
    except:
        t2675 = None
    try:
        t2676 = fill(I, t2147, t2591)
    except:
        t2676 = None
    if t2676 == O:
        return True, f'776ffc46 - t2676'
    try:
        t2677 = shift(t2594, UNITY)
    except:
        t2677 = None
    try:
        t2678 = mapply(t2503, t29)
    except:
        t2678 = None
    try:
        t2679 = fill(I, t246, t2595)
    except:
        t2679 = None
    if t2679 == O:
        return True, f'7447852a - t2679'
    try:
        t2680 = compose(initset, t689)
    except:
        t2680 = None
    try:
        t2681 = sfilter_f(t1837, t2596)
    except:
        t2681 = None
    try:
        t2682 = shift(t675, t2597)
    except:
        t2682 = None
    try:
        t2683 = fork(either, t2510, t2600)
    except:
        t2683 = None
    try:
        t2684 = connect(t2410, t2601)
    except:
        t2684 = None
    try:
        t2685 = sfilter(t2296, t2602)
    except:
        t2685 = None
    try:
        t2686 = lbind(shift, t1857)
    except:
        t2686 = None
    try:
        t2687 = insert(t689, t2605)
    except:
        t2687 = None
    try:
        t2688 = col_row(t2606, R1)
    except:
        t2688 = None
    try:
        t2689 = fork(subtract, t2416, t2607)
    except:
        t2689 = None
    try:
        t2690 = get_nth_t(t2022, L1)
    except:
        t2690 = None
    try:
        t2691 = apply(t713, t2609)
    except:
        t2691 = None
    try:
        t2692 = t340(t2610)
    except:
        t2692 = None
    try:
        t2693 = crop(t2420, DOWN, t1582)
    except:
        t2693 = None
    try:
        t2694 = apply(t713, t2612)
    except:
        t2694 = None
    try:
        t2695 = apply(t2613, t174)
    except:
        t2695 = None
    try:
        t2696 = underfill(t720, t526, t2614)
    except:
        t2696 = None
    try:
        t2697 = lbind(multiply, t2615)
    except:
        t2697 = None
    try:
        t2698 = hsplit(t2616, t68)
    except:
        t2698 = None
    try:
        t2699 = underfill(t261, t246, t2617)
    except:
        t2699 = None
    try:
        t2700 = sfilter_f(t354, t2618)
    except:
        t2700 = None
    try:
        t2701 = paint(t523, t2619)
    except:
        t2701 = None
    try:
        t2702 = add(t1889, t2620)
    except:
        t2702 = None
    try:
        t2703 = contained(ZERO_BY_TWO, t357)
    except:
        t2703 = None
    try:
        t2704 = compose(t191, t2623)
    except:
        t2704 = None
    try:
        t2705 = branch(t359, I, t2624)
    except:
        t2705 = None
    if t2705 == O:
        return True, f'4938f0c2 - t2705'
    try:
        t2706 = fork(other, palette_f, t937)
    except:
        t2706 = None
    try:
        t2707 = astuple(ONE, TWO)
    except:
        t2707 = None
    try:
        t2708 = sfilter_f(t2438, t1683)
    except:
        t2708 = None
    try:
        t2709 = compose(t2627, t10)
    except:
        t2709 = None
    try:
        t2710 = lbind(subtract, t47)
    except:
        t2710 = None
    try:
        t2711 = fill(t948, t1907, t2628)
    except:
        t2711 = None
    try:
        t2712 = branch(t2629, t2207, t2443)
    except:
        t2712 = None
    try:
        t2713 = vconcat(t2062, t2630)
    except:
        t2713 = None
    if t2713 == O:
        return True, f'a61ba2ce - t2713'
    try:
        t2714 = subtract(t2631, TEN)
    except:
        t2714 = None
    try:
        t2715 = get_nth_t(t2544, L1)
    except:
        t2715 = None
    try:
        t2716 = fill(t573, t807, t2633)
    except:
        t2716 = None
    try:
        t2717 = fork(manhattan, initset, t2635)
    except:
        t2717 = None
    try:
        t2718 = compose(t438, t398)
    except:
        t2718 = None
    try:
        t2719 = fill(t2080, RED, t2636)
    except:
        t2719 = None
    try:
        t2720 = shift(t2549, t829)
    except:
        t2720 = None
    try:
        t2721 = recolor_o(RED, t2637)
    except:
        t2721 = None
    try:
        t2722 = apply(t835, t2638)
    except:
        t2722 = None
    try:
        t2723 = compose(decrement, t2639)
    except:
        t2723 = None
    try:
        t2724 = shift(t99, t2640)
    except:
        t2724 = None
    try:
        t2725 = recolor_i(BLACK, t2643)
    except:
        t2725 = None
    try:
        t2726 = decrement(t2646)
    except:
        t2726 = None
    try:
        t2727 = fill(t2561, t1410, t2647)
    except:
        t2727 = None
    if t2727 == O:
        return True, f'b782dc8a - t2727'
    try:
        t2728 = fork(apply, t2466, t2648)
    except:
        t2728 = None
    try:
        t2729 = mapply(vfrontier, t2649)
    except:
        t2729 = None
    try:
        t2730 = get_color_rank_f(t2360, L1)
    except:
        t2730 = None
    try:
        t2731 = paint(t598, t2650)
    except:
        t2731 = None
    try:
        t2732 = position(t126, t599)
    except:
        t2732 = None
    try:
        t2733 = matcher(t602, t2652)
    except:
        t2733 = None
    try:
        t2734 = mapply(hfrontier, t2653)
    except:
        t2734 = None
    try:
        t2735 = shift(t2567, t2654)
    except:
        t2735 = None
    try:
        t2736 = t1788(ONE)
    except:
        t2736 = None
    try:
        t2737 = rbind(repeat, t2655)
    except:
        t2737 = None
    try:
        t2738 = rbind(multiply, t2656)
    except:
        t2738 = None
    try:
        t2739 = mapply(t4, t2657)
    except:
        t2739 = None
    try:
        t2740 = mapply(neighbors, t2658)
    except:
        t2740 = None
    try:
        t2741 = decrement(t2659)
    except:
        t2741 = None
    try:
        t2742 = subtract(t2119, t2660)
    except:
        t2742 = None
    try:
        t2743 = rbind(sfilter, t2662)
    except:
        t2743 = None
    try:
        t2744 = paint(t831, t2663)
    except:
        t2744 = None
    if t2744 == O:
        return True, f'49d1d64f - t2744'
    try:
        t2745 = chain(t905, t633, t1630)
    except:
        t2745 = None
    try:
        t2746 = switch(t282, RED, BLACK)
    except:
        t2746 = None
    try:
        t2747 = product(t2666, t2666)
    except:
        t2747 = None
    try:
        t2748 = apply(t1636, t2667)
    except:
        t2748 = None
    try:
        t2749 = remove_f(t1463, t1258)
    except:
        t2749 = None
    try:
        t2750 = hconcat(t2671, t1989)
    except:
        t2750 = None
    try:
        t2751 = apply(toindices, t2673)
    except:
        t2751 = None
    try:
        t2752 = shift(t2674, RIGHT)
    except:
        t2752 = None
    try:
        t2753 = subtract(t2589, t2675)
    except:
        t2753 = None
    try:
        t2754 = paint(t1062, t2677)
    except:
        t2754 = None
    if t2754 == O:
        return True, f'846bdb03 - t2754'
    try:
        t2755 = fill(t2284, BLUE, t2678)
    except:
        t2755 = None
    if t2755 == O:
        return True, f'8d510a79 - t2755'
    try:
        t2756 = fork(insert, t105, t2680)
    except:
        t2756 = None
    try:
        t2757 = mapply(t2116, t2681)
    except:
        t2757 = None
    try:
        t2758 = paint(I, t2682)
    except:
        t2758 = None
    try:
        t2759 = compose(t2683, initset)
    except:
        t2759 = None
    try:
        t2760 = combine_f(t1852, t2684)
    except:
        t2760 = None
    try:
        t2761 = shift(t6, UNITY)
    except:
        t2761 = None
    try:
        t2762 = mir_rot_t(t2685, R4)
    except:
        t2762 = None
    try:
        t2763 = insert(t2603, t12)
    except:
        t2763 = None
    try:
        t2764 = lbind(multiply, t692)
    except:
        t2764 = None
    try:
        t2765 = insert(t2286, t2687)
    except:
        t2765 = None
    try:
        t2766 = matcher(t10, t2688)
    except:
        t2766 = None
    try:
        t2767 = fork(shift, identity, t2689)
    except:
        t2767 = None
    try:
        t2768 = greater(t2690, SEVEN)
    except:
        t2768 = None
    try:
        t2769 = lbind(compose, t1323)
    except:
        t2769 = None
    try:
        t2770 = mir_rot_t(t2693, R2)
    except:
        t2770 = None
    try:
        t2771 = papply(connect, t2421, t2695)
    except:
        t2771 = None
    try:
        t2772 = lbind(chain, backdrop)
    except:
        t2772 = None
    try:
        t2773 = interval(ONE, FIVE, ONE)
    except:
        t2773 = None
    try:
        t2774 = merge_t(t2698)
    except:
        t2774 = None
    if t2774 == O:
        return True, f'91413438 - t2774'
    try:
        t2775 = o_g(t2699, R5)
    except:
        t2775 = None
    try:
        t2776 = mapply(t2042, t2700)
    except:
        t2776 = None
    try:
        t2777 = t345(t2701)
    except:
        t2777 = None
    if t2777 == O:
        return True, f'0a938d79 - t2777'
    try:
        t2778 = t4(t2702)
    except:
        t2778 = None
    try:
        t2779 = mir_rot_t(t2316, R4)
    except:
        t2779 = None
    try:
        t2780 = fork(mapply, t21, t2704)
    except:
        t2780 = None
    try:
        t2781 = difference(t1545, t2052)
    except:
        t2781 = None
    try:
        t2782 = initset(DOWN)
    except:
        t2782 = None
    try:
        t2783 = mapply(t2324, t2708)
    except:
        t2783 = None
    try:
        t2784 = chain(increment, t2710, height_f)
    except:
        t2784 = None
    try:
        t2785 = color(t2329)
    except:
        t2785 = None
    try:
        t2786 = fill(t1155, t1737, t2712)
    except:
        t2786 = None
    if t2786 == O:
        return True, f'5daaa586 - t2786'
    try:
        t2787 = add(t2631, TEN)
    except:
        t2787 = None
    try:
        t2788 = mir_rot_t(t2715, R2)
    except:
        t2788 = None
    try:
        t2789 = compose(even, t2717)
    except:
        t2789 = None
    try:
        t2790 = fork(equality, t2718, t438)
    except:
        t2790 = None
    try:
        t2791 = get_arg_rank_f(t2452, t302, F0)
    except:
        t2791 = None
    try:
        t2792 = underfill(I, t246, t2720)
    except:
        t2792 = None
    if t2792 == O:
        return True, f'4612dd53 - t2792'
    try:
        t2793 = paint(I, t2721)
    except:
        t2793 = None
    if t2793 == O:
        return True, f'e5062a87 - t2793'
    try:
        t2794 = fork(either, vline_o, hline_o)
    except:
        t2794 = None
    try:
        t2795 = fork(equality, size, t2723)
    except:
        t2795 = None
    try:
        t2796 = branch(t1191, t2345, t2724)
    except:
        t2796 = None
    try:
        t2797 = f_ofcolor(t2641, CYAN)
    except:
        t2797 = None
    try:
        t2798 = apply(t302, t171)
    except:
        t2798 = None
    try:
        t2799 = o_g(t861, R5)
    except:
        t2799 = None
    try:
        t2800 = matcher(t1943, t28)
    except:
        t2800 = None
    try:
        t2801 = increment(t644)
    except:
        t2801 = None
    try:
        t2802 = index(t2560, t2726)
    except:
        t2802 = None
    try:
        t2803 = fork(mapply, t113, t2728)
    except:
        t2803 = None
    try:
        t2804 = fill(t2359, RED, t2729)
    except:
        t2804 = None
    if t2804 == O:
        return True, f'd9f24cd1 - t2804'
    try:
        t2805 = matcher(t10, t2730)
    except:
        t2805 = None
    try:
        t2806 = get_nth_t(t2732, F0)
    except:
        t2806 = None
    try:
        t2807 = extract(t422, t2733)
    except:
        t2807 = None
    try:
        t2808 = fill(t1008, t1216, t2735)
    except:
        t2808 = None
    if t2808 == O:
        return True, f'98cf29f8 - t2808'
    try:
        t2809 = fill(t2568, t264, t2736)
    except:
        t2809 = None
    if t2809 == O:
        return True, f'a85d4709 - t2809'
    try:
        t2810 = apply(t2737, t2569)
    except:
        t2810 = None
    try:
        t2811 = fill(t2371, t2477, t2739)
    except:
        t2811 = None
    if t2811 == O:
        return True, f'8731374e - t2811'
    try:
        t2812 = fill(t2478, CYAN, t2740)
    except:
        t2812 = None
    if t2812 == O:
        return True, f'ecdecbb3 - t2812'
    try:
        t2813 = multiply(t2572, THREE)
    except:
        t2813 = None
    try:
        t2814 = shift(t820, t2742)
    except:
        t2814 = None
    try:
        t2815 = compose(t425, t2574)
    except:
        t2815 = None
    try:
        t2816 = interval(ZERO, t1441, ONE)
    except:
        t2816 = None
    try:
        t2817 = lbind(compose, t2745)
    except:
        t2817 = None
    try:
        t2818 = o_g(t2746, R7)
    except:
        t2818 = None
    try:
        t2819 = underfill(I, t1043, t2747)
    except:
        t2819 = None
    if t2819 == O:
        return True, f'ec883f72 - t2819'
    try:
        t2820 = mapply(t1459, t2748)
    except:
        t2820 = None
    try:
        t2821 = mapply(t2669, t2749)
    except:
        t2821 = None
    try:
        t2822 = vconcat(t2585, t2750)
    except:
        t2822 = None
    try:
        t2823 = astuple(t47, t2279)
    except:
        t2823 = None
    try:
        t2824 = lbind(extract, t2751)
    except:
        t2824 = None
    try:
        t2825 = compose(t298, t1309)
    except:
        t2825 = None
    try:
        t2826 = fill(t2144, t246, t2752)
    except:
        t2826 = None
    if t2826 == O:
        return True, f'29c11459 - t2826'
    try:
        t2827 = shoot(t2589, t2753)
    except:
        t2827 = None
    try:
        t2828 = fork(insert, t15, t2756)
    except:
        t2828 = None
    try:
        t2829 = fill(t2154, t246, t2757)
    except:
        t2829 = None
    try:
        t2830 = move(t2758, t1288, t1841)
    except:
        t2830 = None
    if t2830 == O:
        return True, f'56dc2b01 - t2830'
    try:
        t2831 = astuple(FIVE, FIVE)
    except:
        t2831 = None
    try:
        t2832 = sfilter_f(t26, t2759)
    except:
        t2832 = None
    try:
        t2833 = underfill(I, CYAN, t2760)
    except:
        t2833 = None
    if t2833 == O:
        return True, f'a2fd1cf0 - t2833'
    try:
        t2834 = fill(t2512, t264, t2761)
    except:
        t2834 = None
    if t2834 == O:
        return True, f'a9f96cdd - t2834'
    try:
        t2835 = sfilter(t2762, t2602)
    except:
        t2835 = None
    try:
        t2836 = compose(t1306, palette_f)
    except:
        t2836 = None
    try:
        t2837 = insert(t15, t2765)
    except:
        t2837 = None
    try:
        t2838 = col_row(t2606, R0)
    except:
        t2838 = None
    try:
        t2839 = compose(t1101, t2299)
    except:
        t2839 = None
    try:
        t2840 = greater(t2690, THREE)
    except:
        t2840 = None
    try:
        t2841 = apply(t721, t2609)
    except:
        t2841 = None
    try:
        t2842 = vconcat(t2611, t2770)
    except:
        t2842 = None
    try:
        t2843 = apply(t721, t2612)
    except:
        t2843 = None
    try:
        t2844 = apply(t23, t2421)
    except:
        t2844 = None
    try:
        t2845 = lbind(t2772, inbox)
    except:
        t2845 = None
    try:
        t2846 = apply(t2697, t2773)
    except:
        t2846 = None
    try:
        t2847 = underfill(I, t726, t2776)
    except:
        t2847 = None
    if t2847 == O:
        return True, f'6d58a25d - t2847'
    try:
        t2848 = fill(t130, t1349, t2778)
    except:
        t2848 = None
    if t2848 == O:
        return True, f'e48d4e1a - t2848'
    try:
        t2849 = branch(t2703, t2779, t2316)
    except:
        t2849 = None
    try:
        t2850 = apply(t2432, t1503)
    except:
        t2850 = None
    try:
        t2851 = lbind(rbind, upscale_f)
    except:
        t2851 = None
    try:
        t2852 = lbind(shift, t2781)
    except:
        t2852 = None
    try:
        t2853 = insert(UNITY, t2782)
    except:
        t2853 = None
    try:
        t2854 = fill(t1145, BLACK, t2783)
    except:
        t2854 = None
    try:
        t2855 = compose(t1147, t342)
    except:
        t2855 = None
    try:
        t2856 = compose(t2536, t2784)
    except:
        t2856 = None
    try:
        t2857 = centerofmass(t2628)
    except:
        t2857 = None
    try:
        t2858 = rbind(shoot, DOWN_LEFT)
    except:
        t2858 = None
    try:
        t2859 = interval(t2714, t2787, TWO)
    except:
        t2859 = None
    try:
        t2860 = vconcat(t2632, t2788)
    except:
        t2860 = None
    try:
        t2861 = sfilter_f(t1924, t2789)
    except:
        t2861 = None
    try:
        t2862 = fork(add, t2548, t2790)
    except:
        t2862 = None
    try:
        t2863 = fill(t2719, BLUE, t2791)
    except:
        t2863 = None
    try:
        t2864 = mfilter_f(t2722, t2794)
    except:
        t2864 = None
    try:
        t2865 = mfilter_f(t7, t2795)
    except:
        t2865 = None
    try:
        t2866 = paint(t988, t2796)
    except:
        t2866 = None
    if t2866 == O:
        return True, f'53b68214 - t2866'
    try:
        t2867 = mapply(t14, t2797)
    except:
        t2867 = None
    try:
        t2868 = t2642(t2798)
    except:
        t2868 = None
    try:
        t2869 = insert(t2725, t2799)
    except:
        t2869 = None
    try:
        t2870 = compose(t1594, t2800)
    except:
        t2870 = None
    try:
        t2871 = shift(t2645, t2801)
    except:
        t2871 = None
    try:
        t2872 = replace(t2560, t251, t2802)
    except:
        t2872 = None
    try:
        t2873 = sfilter_f(t2468, t2805)
    except:
        t2873 = None
    try:
        t2874 = fork(combine, identity, t689)
    except:
        t2874 = None
    try:
        t2875 = branch(t805, t2806, ZERO)
    except:
        t2875 = None
    try:
        t2876 = corner(t2566, R0)
    except:
        t2876 = None
    try:
        t2877 = t2249(t49)
    except:
        t2877 = None
    try:
        t2878 = t1789(t2810)
    except:
        t2878 = None
    if t2878 == O:
        return True, f'8e1813be - t2878'
    try:
        t2879 = lbind(astuple, BURGUNDY)
    except:
        t2879 = None
    try:
        t2880 = add(t2813, TWO_BY_TWO)
    except:
        t2880 = None
    try:
        t2881 = paint(I, t2814)
    except:
        t2881 = None
    try:
        t2882 = branch(t826, t2661, t2815)
    except:
        t2882 = None
    try:
        t2883 = rbind(pair, t2816)
    except:
        t2883 = None
    try:
        t2884 = astuple(t2286, t689)
    except:
        t2884 = None
    try:
        t2885 = lbind(lbind, astuple)
    except:
        t2885 = None
    try:
        t2886 = apply(toindices, t2818)
    except:
        t2886 = None
    try:
        t2887 = rbind(add, DOWN_LEFT)
    except:
        t2887 = None
    try:
        t2888 = replace(t2581, t2668, t246)
    except:
        t2888 = None
    try:
        t2889 = underfill(I, ONE, t2821)
    except:
        t2889 = None
    if t2889 == O:
        return True, f'90f3ed37 - t2889'
    try:
        t2890 = asobject(t2822)
    except:
        t2890 = None
    try:
        t2891 = crop(t2672, ORIGIN, t2823)
    except:
        t2891 = None
    try:
        t2892 = lbind(matcher, normalize)
    except:
        t2892 = None
    try:
        t2893 = fork(subtract, t298, t2825)
    except:
        t2893 = None
    try:
        t2894 = underfill(I, ONE, t2827)
    except:
        t2894 = None
    try:
        t2895 = fork(insert, t2286, t2828)
    except:
        t2895 = None
    try:
        t2896 = power(outbox, THREE)
    except:
        t2896 = None
    try:
        t2897 = t1494(t2831)
    except:
        t2897 = None
    try:
        t2898 = difference(t26, t2832)
    except:
        t2898 = None
    try:
        t2899 = mir_rot_t(t2835, R6)
    except:
        t2899 = None
    if t2899 == O:
        return True, f'780d0b14 - t2899'
    try:
        t2900 = sfilter_f(t2763, t2836)
    except:
        t2900 = None
    try:
        t2901 = interval(ZERO, THREE, ONE)
    except:
        t2901 = None
    try:
        t2902 = insert(t105, t2837)
    except:
        t2902 = None
    try:
        t2903 = matcher(t10, t2838)
    except:
        t2903 = None
    try:
        t2904 = chain(positive, size, t2839)
    except:
        t2904 = None
    try:
        t2905 = branch(t2840, FOUR, ZERO)
    except:
        t2905 = None
    try:
        t2906 = combine_f(t2691, t2841)
    except:
        t2906 = None
    try:
        t2907 = fork(position, t1323, t1868)
    except:
        t2907 = None
    try:
        t2908 = crop(t2420, TWO_BY_ZERO, t1582)
    except:
        t2908 = None
    try:
        t2909 = combine_f(t2694, t2843)
    except:
        t2909 = None
    try:
        t2910 = pair(t2771, t2844)
    except:
        t2910 = None
    try:
        t2911 = compose(t2845, t1530)
    except:
        t2911 = None
    try:
        t2912 = mapply(t349, t2846)
    except:
        t2912 = None
    try:
        t2913 = get_arg_rank_f(t2775, t721, F0)
    except:
        t2913 = None
    try:
        t2914 = branch(t2529, t2622, t2849)
    except:
        t2914 = None
    try:
        t2915 = mapply(t1892, t2850)
    except:
        t2915 = None
    try:
        t2916 = interval(ONE, FOUR, ONE)
    except:
        t2916 = None
    try:
        t2917 = compose(t2852, t2435)
    except:
        t2917 = None
    try:
        t2918 = insert(t2707, t2853)
    except:
        t2918 = None
    try:
        t2919 = t943(t2854)
    except:
        t2919 = None
    if t2919 == O:
        return True, f'855e0971 - t2919'
    try:
        t2920 = fork(sfilter, identity, t2855)
    except:
        t2920 = None
    try:
        t2921 = connect(t2442, t2857)
    except:
        t2921 = None
    try:
        t2922 = rbind(shoot, UP_RIGHT)
    except:
        t2922 = None
    try:
        t2923 = rbind(contained, t2859)
    except:
        t2923 = None
    try:
        t2924 = fork(subtract, t23, t10)
    except:
        t2924 = None
    try:
        t2925 = fill(t1389, GRAY, t2861)
    except:
        t2925 = None
    if t2925 == O:
        return True, f'f35d900a - t2925'
    try:
        t2926 = fork(astuple, t2079, t2862)
    except:
        t2926 = None
    try:
        t2927 = lbind(hmatching, t1929)
    except:
        t2927 = None
    try:
        t2928 = paint(I, t2864)
    except:
        t2928 = None
    try:
        t2929 = fill(t2455, t246, t2865)
    except:
        t2929 = None
    if t2929 == O:
        return True, f'e509e548 - t2929'
    try:
        t2930 = lbind(sfilter, t2867)
    except:
        t2930 = None
    try:
        t2931 = toivec(t2868)
    except:
        t2931 = None
    try:
        t2932 = fork(add, t2644, t2870)
    except:
        t2932 = None
    try:
        t2933 = branch(t999, tojvec, toivec)
    except:
        t2933 = None
    try:
        t2934 = t1203(t2356, t2872)
    except:
        t2934 = None
    if t2934 == O:
        return True, f'2204b7a8 - t2934'
    try:
        t2935 = corner(t2873, R0)
    except:
        t2935 = None
    try:
        t2936 = get_nth_t(t2732, L1)
    except:
        t2936 = None
    try:
        t2937 = corner(t2807, R0)
    except:
        t2937 = None
    try:
        t2938 = pair(t2877, t1215)
    except:
        t2938 = None
    try:
        t2939 = apply(t2738, t967)
    except:
        t2939 = None
    try:
        t2940 = add(t609, THREE)
    except:
        t2940 = None
    try:
        t2941 = crop(I, t2741, t2880)
    except:
        t2941 = None
    try:
        t2942 = o_g(t2881, R3)
    except:
        t2942 = None
    try:
        t2943 = width_f(t108)
    except:
        t2943 = None
    try:
        t2944 = replace(t2575, t251, t246)
    except:
        t2944 = None
    if t2944 == O:
        return True, f'f8c80d96 - t2944'
    try:
        t2945 = chain(t270, t2743, t2883)
    except:
        t2945 = None
    try:
        t2946 = combine(t2664, t2884)
    except:
        t2946 = None
    try:
        t2947 = compose(t2817, t2885)
    except:
        t2947 = None
    try:
        t2948 = lbind(sfilter, t2886)
    except:
        t2948 = None
    try:
        t2949 = c_iz_n(S, t1, t1680)
    except:
        t2949 = None
    try:
        t2950 = apply(t721, t729)
    except:
        t2950 = None
    try:
        t2951 = paint(t296, t2890)
    except:
        t2951 = None
    if t2951 == O:
        return True, f'539a4f51 - t2951'
    try:
        t2952 = mir_rot_t(t2891, R0)
    except:
        t2952 = None
    try:
        t2953 = chain(t298, t2824, t2892)
    except:
        t2953 = None
    try:
        t2954 = compose(t2588, t2893)
    except:
        t2954 = None
    try:
        t2955 = o_g(t2894, R4)
    except:
        t2955 = None
    try:
        t2956 = compose(t2153, t2895)
    except:
        t2956 = None
    try:
        t2957 = matcher(t2505, t246)
    except:
        t2957 = None
    try:
        t2958 = fill(t2599, t264, t2897)
    except:
        t2958 = None
    if t2958 == O:
        return True, f'941d9a10 - t2958'
    try:
        t2959 = canvas(t251, t1582)
    except:
        t2959 = None
    try:
        t2960 = cover(t2012, t2898)
    except:
        t2960 = None
    if t2960 == O:
        return True, f'e21d9049 - t2960'
    try:
        t2961 = get_arg_rank_f(t2900, size, F0)
    except:
        t2961 = None
    try:
        t2962 = product(t2901, t2901)
    except:
        t2962 = None
    try:
        t2963 = fork(either, t2766, t2903)
    except:
        t2963 = None
    try:
        t2964 = sfilter_f(t1513, t2904)
    except:
        t2964 = None
    try:
        t2965 = branch(t2768, EIGHT, t2905)
    except:
        t2965 = None
    try:
        t2966 = cover(t2302, t2906)
    except:
        t2966 = None
    try:
        t2967 = chain(toivec, t10, t2907)
    except:
        t2967 = None
    try:
        t2968 = vconcat(t2842, t2908)
    except:
        t2968 = None
    if t2968 == O:
        return True, f'cdecee7f - t2968'
    try:
        t2969 = cover(t2306, t2909)
    except:
        t2969 = None
    try:
        t2970 = mapply(t1702, t2910)
    except:
        t2970 = None
    try:
        t2971 = lbind(apply, initset)
    except:
        t2971 = None
    try:
        t2972 = fill(I, t2, t2912)
    except:
        t2972 = None
    if t2972 == O:
        return True, f'e8dc4411 - t2972'
    try:
        t2973 = paint(t2699, t2913)
    except:
        t2973 = None
    if t2973 == O:
        return True, f'469497ad - t2973'
    try:
        t2974 = branch(t535, t2430, t2914)
    except:
        t2974 = None
    if t2974 == O:
        return True, f'4522001f - t2974'
    try:
        t2975 = paint(I, t2915)
    except:
        t2975 = None
    if t2975 == O:
        return True, f'caa06a1f - t2975'
    try:
        t2976 = apply(t2851, t2916)
    except:
        t2976 = None
    try:
        t2977 = fork(recolor_o, t2706, t2917)
    except:
        t2977 = None
    try:
        t2978 = insert(t2626, t2918)
    except:
        t2978 = None
    try:
        t2979 = fork(t193, t2920, t2439)
    except:
        t2979 = None
    try:
        t2980 = lbind(subtract, t74)
    except:
        t2980 = None
    try:
        t2981 = fill(t2711, t2785, t2921)
    except:
        t2981 = None
    try:
        t2982 = fork(combine, t2858, t2922)
    except:
        t2982 = None
    try:
        t2983 = canvas(BLACK, t1582)
    except:
        t2983 = None
    try:
        t2984 = fork(shoot, t10, t2924)
    except:
        t2984 = None
    try:
        t2985 = fork(shoot, t577, t2926)
    except:
        t2985 = None
    try:
        t2986 = sfilter_f(t2224, t2927)
    except:
        t2986 = None
    try:
        t2987 = shift(t73, t2931)
    except:
        t2987 = None
    try:
        t2988 = order(t2869, t302)
    except:
        t2988 = None
    try:
        t2989 = fork(add, t2353, t2932)
    except:
        t2989 = None
    try:
        t2990 = compose(t2933, increment)
    except:
        t2990 = None
    try:
        t2991 = lbind(multiply, t2935)
    except:
        t2991 = None
    try:
        t2992 = branch(t805, ZERO, t2936)
    except:
        t2992 = None
    try:
        t2993 = subtract(t2876, t2937)
    except:
        t2993 = None
    try:
        t2994 = mapply(t1429, t2939)
    except:
        t2994 = None
    try:
        t2995 = interval(t2940, TEN, FOUR)
    except:
        t2995 = None
    try:
        t2996 = asobject(t2941)
    except:
        t2996 = None
    try:
        t2997 = get_nth_f(t2942, F0)
    except:
        t2997 = None
    try:
        t2998 = equality(t2943, FIVE)
    except:
        t2998 = None
    try:
        t2999 = compose(t18, t2945)
    except:
        t2999 = None
    try:
        t3000 = compose(t2577, t2947)
    except:
        t3000 = None
    try:
        t3001 = difference(t2134, t2580)
    except:
        t3001 = None
    try:
        t3002 = fill(t2670, t1853, t2950)
    except:
        t3002 = None
    if t3002 == O:
        return True, f'95990924 - t3002'
    try:
        t3003 = compose(t2953, toindices)
    except:
        t3003 = None
    try:
        t3004 = colorfilter(t2955, ONE)
    except:
        t3004 = None
    try:
        t3005 = rbind(branch, NEG_TWO)
    except:
        t3005 = None
    try:
        t3006 = sfilter_f(t1837, t2957)
    except:
        t3006 = None
    try:
        t3007 = o_g(t2598, R5)
    except:
        t3007 = None
    try:
        t3008 = asobject(t2959)
    except:
        t3008 = None
    try:
        t3009 = mir_rot_f(t2961, R2)
    except:
        t3009 = None
    try:
        t3010 = totuple(t2962)
    except:
        t3010 = None
    try:
        t3011 = sfilter_f(t2415, t2963)
    except:
        t3011 = None
    try:
        t3012 = apply(t2767, t2964)
    except:
        t3012 = None
    try:
        t3013 = astuple(t2608, t2965)
    except:
        t3013 = None
    try:
        t3014 = fork(multiply, shape_f, t2967)
    except:
        t3014 = None
    try:
        t3015 = fill(I, BLACK, t2970)
    except:
        t3015 = None
    if t3015 == O:
        return True, f'3bdb4ada - t3015'
    try:
        t3016 = chain(t2971, corners, t2422)
    except:
        t3016 = None
    try:
        t3017 = fork(combine, t2625, t2977)
    except:
        t3017 = None
    try:
        t3018 = fill(t2534, BLACK, t2978)
    except:
        t3018 = None
    try:
        t3019 = compose(t23, t2979)
    except:
        t3019 = None
    try:
        t3020 = chain(increment, t2980, width_f)
    except:
        t3020 = None
    try:
        t3021 = add(t2857, DOWN)
    except:
        t3021 = None
    try:
        t3022 = fork(combine, t1459, t2982)
    except:
        t3022 = None
    try:
        t3023 = compose(t2923, t23)
    except:
        t3023 = None
    try:
        t3024 = vconcat(t2860, t2983)
    except:
        t3024 = None
    if t3024 == O:
        return True, f'b0c4d837 - t3024'
    try:
        t3025 = corners(t1924)
    except:
        t3025 = None
    try:
        t3026 = f_ofcolor(I, t50)
    except:
        t3026 = None
    try:
        t3027 = mapply(hfrontier, t2987)
    except:
        t3027 = None
    try:
        t3028 = remove_f(t2725, t2988)
    except:
        t3028 = None
    try:
        t3029 = compose(t58, t2989)
    except:
        t3029 = None
    try:
        t3030 = branch(t999, width_f, height_f)
    except:
        t3030 = None
    try:
        t3031 = compose(t2991, width_f)
    except:
        t3031 = None
    try:
        t3032 = astuple(t2875, t2992)
    except:
        t3032 = None
    try:
        t3033 = move(t2471, t2807, t2993)
    except:
        t3033 = None
    if t3033 == O:
        return True, f'228f6490 - t3033'
    try:
        t3034 = sfilter_t(t2938, t10)
    except:
        t3034 = None
    try:
        t3035 = paint(I, t2994)
    except:
        t3035 = None
    try:
        t3036 = apply(t2879, t2995)
    except:
        t3036 = None
    try:
        t3037 = lbind(shift, t2996)
    except:
        t3037 = None
    try:
        t3038 = subgrid(t2997, t2881)
    except:
        t3038 = None
    try:
        t3039 = branch(t2998, t2815, t2661)
    except:
        t3039 = None
    try:
        t3040 = power(t2999, TWO)
    except:
        t3040 = None
    try:
        t3041 = rbind(compose, t3000)
    except:
        t3041 = None
    try:
        t3042 = chain(t2665, t2948, t1293)
    except:
        t3042 = None
    try:
        t3043 = apply(t713, t3001)
    except:
        t3043 = None
    try:
        t3044 = replace(t2888, t2949, t264)
    except:
        t3044 = None
    if t3044 == O:
        return True, f'54d9e175 - t3044'
    try:
        t3045 = fork(shift, identity, t3003)
    except:
        t3045 = None
    try:
        t3046 = fork(apply, t2954, t1510)
    except:
        t3046 = None
    try:
        t3047 = rbind(adjacent, t42)
    except:
        t3047 = None
    try:
        t3048 = fork(t3005, positive, decrement)
    except:
        t3048 = None
    try:
        t3049 = mapply(t2896, t3006)
    except:
        t3049 = None
    try:
        t3050 = rbind(adjacent, t187)
    except:
        t3050 = None
    try:
        t3051 = lbind(shift, t3008)
    except:
        t3051 = None
    try:
        t3052 = t1856(t3009)
    except:
        t3052 = None
    try:
        t3053 = apply(t10, t3010)
    except:
        t3053 = None
    try:
        t3054 = mapply(vfrontier, t3011)
    except:
        t3054 = None
    try:
        t3055 = compose(decrement, width_f)
    except:
        t3055 = None
    try:
        t3056 = crop(I, t3013, THREE_BY_THREE)
    except:
        t3056 = None
    try:
        t3057 = fork(shift, t2286, t3014)
    except:
        t3057 = None
    try:
        t3058 = fork(mapply, t2911, t3016)
    except:
        t3058 = None
    try:
        t3059 = get_arg_rank_f(t12, numcolors_f, F0)
    except:
        t3059 = None
    try:
        t3060 = remove_f(t118, t12)
    except:
        t3060 = None
    try:
        t3061 = vupscale(t75, FIVE)
    except:
        t3061 = None
    try:
        t3062 = chain(t3019, t10, t23)
    except:
        t3062 = None
    try:
        t3063 = compose(t2536, t3020)
    except:
        t3063 = None
    try:
        t3064 = initset(t2857)
    except:
        t3064 = None
    try:
        t3065 = compose(t3022, center)
    except:
        t3065 = None
    try:
        t3066 = sfilter_f(t2543, t3023)
    except:
        t3066 = None
    try:
        t3067 = f_ofcolor(t2716, BLACK)
    except:
        t3067 = None
    try:
        t3068 = mapply(t2985, t17)
    except:
        t3068 = None
    try:
        t3069 = get_arg_rank_f(t2986, t342, L1)
    except:
        t3069 = None
    try:
        t3070 = fill(t2928, t50, t3026)
    except:
        t3070 = None
    if t3070 == O:
        return True, f'06df4c85 - t3070'
    try:
        t3071 = underfill(t2351, CYAN, t3027)
    except:
        t3071 = None
    if t3071 == O:
        return True, f'673ef223 - t3071'
    try:
        t3072 = get_nth_t(t2988, F0)
    except:
        t3072 = None
    try:
        t3073 = t3030(t2645)
    except:
        t3073 = None
    try:
        t3074 = fork(subtract, t298, t3031)
    except:
        t3074 = None
    try:
        t3075 = t921(t2564)
    except:
        t3075 = None
    try:
        t3076 = multiply(t2651, t3032)
    except:
        t3076 = None
    try:
        t3077 = mapply(vfrontier, t3034)
    except:
        t3077 = None
    try:
        t3078 = subgrid(t427, t3035)
    except:
        t3078 = None
    if t3078 == O:
        return True, f'f9012d9b - t3078'
    try:
        t3079 = fill(t2370, t807, t3036)
    except:
        t3079 = None
    if t3079 == O:
        return True, f'8403a5d5 - t3079'
    try:
        t3080 = increment(t2572)
    except:
        t3080 = None
    try:
        t3081 = mir_rot_t(t3038, R2)
    except:
        t3081 = None
    try:
        t3082 = fork(combine, t2882, t3039)
    except:
        t3082 = None
    try:
        t3083 = rbind(toobject, t1235)
    except:
        t3083 = None
    try:
        t3084 = product(t2946, t2946)
    except:
        t3084 = None
    try:
        t3085 = rbind(sfilter, t3042)
    except:
        t3085 = None
    try:
        t3086 = apply(t2887, t3043)
    except:
        t3086 = None
    try:
        t3087 = replace(I, FIVE, ZERO)
    except:
        t3087 = None
    try:
        t3088 = fork(mapply, t113, t3046)
    except:
        t3088 = None
    try:
        t3089 = sfilter_f(t3004, t3047)
    except:
        t3089 = None
    try:
        t3090 = fill(t2829, t246, t3049)
    except:
        t3090 = None
    if t3090 == O:
        return True, f'db93a21d - t3090'
    try:
        t3091 = extract(t3007, t3050)
    except:
        t3091 = None
    try:
        t3092 = occurrences(t2407, t3008)
    except:
        t3092 = None
    try:
        t3093 = remove_f(t2961, t2900)
    except:
        t3093 = None
    try:
        t3094 = apply(t2764, t3053)
    except:
        t3094 = None
    try:
        t3095 = product(t2902, t2976)
    except:
        t3095 = None
    try:
        t3096 = difference(t2415, t3011)
    except:
        t3096 = None
    try:
        t3097 = chain(positive, decrement, t3055)
    except:
        t3097 = None
    try:
        t3098 = replace(t3056, FIVE, ZERO)
    except:
        t3098 = None
    try:
        t3099 = rbind(sfilter, t1039)
    except:
        t3099 = None
    try:
        t3100 = t2769(t3057)
    except:
        t3100 = None
    try:
        t3101 = fork(intersection, t2422, t3058)
    except:
        t3101 = None
    try:
        t3102 = normalize(t3059)
    except:
        t3102 = None
    try:
        t3103 = mapply(t3017, t3060)
    except:
        t3103 = None
    try:
        t3104 = hupscale(t3061, THREE)
    except:
        t3104 = None
    try:
        t3105 = fork(subtract, t2709, t3062)
    except:
        t3105 = None
    try:
        t3106 = fork(product, t2856, t3063)
    except:
        t3106 = None
    try:
        t3107 = insert(t3021, t3064)
    except:
        t3107 = None
    try:
        t3108 = mapply(t3065, t209)
    except:
        t3108 = None
    try:
        t3109 = fill(t763, t807, t3066)
    except:
        t3109 = None
    if t3109 == O:
        return True, f'834ec97d - t3109'
    try:
        t3110 = rbind(colorcount_f, BLACK)
    except:
        t3110 = None
    try:
        t3111 = fill(I, TWO, t3068)
    except:
        t3111 = None
    try:
        t3112 = fill(t2863, YELLOW, t3069)
    except:
        t3112 = None
    try:
        t3113 = chain(decrement, t10, t10)
    except:
        t3113 = None
    try:
        t3114 = remove_f(t3072, t2988)
    except:
        t3114 = None
    try:
        t3115 = apply(t3029, t33)
    except:
        t3115 = None
    try:
        t3116 = t2990(t3073)
    except:
        t3116 = None
    try:
        t3117 = compose(t2563, t3074)
    except:
        t3117 = None
    try:
        t3118 = t2874(t3075)
    except:
        t3118 = None
    try:
        t3119 = add(t2565, t3076)
    except:
        t3119 = None
    try:
        t3120 = astuple(t2734, t3077)
    except:
        t3120 = None
    try:
        t3121 = rbind(subtract, t3080)
    except:
        t3121 = None
    try:
        t3122 = o_g(t3081, R3)
    except:
        t3122 = None
    try:
        t3123 = compose(t1806, t3082)
    except:
        t3123 = None
    try:
        t3124 = chain(t3083, corners, outbox)
    except:
        t3124 = None
    try:
        t3125 = apply(t2018, t3084)
    except:
        t3125 = None
    try:
        t3126 = chain(t117, t3041, t708)
    except:
        t3126 = None
    try:
        t3127 = lbind(occurrences, t2746)
    except:
        t3127 = None
    try:
        t3128 = mapply(t1459, t3086)
    except:
        t3128 = None
    try:
        t3129 = o_g(t3087, R5)
    except:
        t3129 = None
    try:
        t3130 = mapply(t3088, t2281)
    except:
        t3130 = None
    try:
        t3131 = difference(t3004, t3089)
    except:
        t3131 = None
    try:
        t3132 = lbind(remove, ZERO)
    except:
        t3132 = None
    try:
        t3133 = get_nth_f(t3091, F0)
    except:
        t3133 = None
    try:
        t3134 = mapply(t3051, t3092)
    except:
        t3134 = None
    try:
        t3135 = mapply(t3052, t3093)
    except:
        t3135 = None
    try:
        t3136 = papply(add, t3094, t3053)
    except:
        t3136 = None
    try:
        t3137 = apply(t2018, t3095)
    except:
        t3137 = None
    try:
        t3138 = mapply(hfrontier, t3096)
    except:
        t3138 = None
    try:
        t3139 = mfilter_f(t3012, t3097)
    except:
        t3139 = None
    try:
        t3140 = asindices(t3098)
    except:
        t3140 = None
    try:
        t3141 = rbind(add, ZERO_BY_TWO)
    except:
        t3141 = None
    try:
        t3142 = compose(crement, invert)
    except:
        t3142 = None
    try:
        t3143 = mapply(t3101, t17)
    except:
        t3143 = None
    try:
        t3144 = rapply_t(t2976, t3102)
    except:
        t3144 = None
    try:
        t3145 = paint(I, t3103)
    except:
        t3145 = None
    if t3145 == O:
        return True, f'82819916 - t3145'
    try:
        t3146 = compose(t547, t3105)
    except:
        t3146 = None
    try:
        t3147 = corner(t945, R0)
    except:
        t3147 = None
    try:
        t3148 = toobject(t3107, t2981)
    except:
        t3148 = None
    try:
        t3149 = intersection(t2541, t3108)
    except:
        t3149 = None
    try:
        t3150 = rbind(toobject, t2716)
    except:
        t3150 = None
    try:
        t3151 = fork(greater, t368, t3113)
    except:
        t3151 = None
    try:
        t3152 = pair(t3028, t3114)
    except:
        t3152 = None
    try:
        t3153 = merge_t(t3115)
    except:
        t3153 = None
    try:
        t3154 = invert(t3116)
    except:
        t3154 = None
    try:
        t3155 = fork(upscale_f, t3117, width_f)
    except:
        t3155 = None
    try:
        t3156 = intersection(t2564, t3118)
    except:
        t3156 = None
    try:
        t3157 = shift(t2470, t3119)
    except:
        t3157 = None
    try:
        t3158 = merge_t(t3120)
    except:
        t3158 = None
    try:
        t3159 = get_nth_f(t3122, F0)
    except:
        t3159 = None
    try:
        t3160 = fork(paint, t442, t3123)
    except:
        t3160 = None
    try:
        t3161 = compose(color, t3124)
    except:
        t3161 = None
    try:
        t3162 = totuple(t3125)
    except:
        t3162 = None
    try:
        t3163 = fork(intersection, t2268, t3126)
    except:
        t3163 = None
    try:
        t3164 = chain(t3127, t2486, normalize)
    except:
        t3164 = None
    try:
        t3165 = combine_f(t2820, t3128)
    except:
        t3165 = None
    try:
        t3166 = replace(t2952, t251, t246)
    except:
        t3166 = None
    if t3166 == O:
        return True, f'e179c5f4 - t3166'
    try:
        t3167 = apply(normalize, t3129)
    except:
        t3167 = None
    try:
        t3168 = paint(t2495, t3130)
    except:
        t3168 = None
    if t3168 == O:
        return True, f'72322fa7 - t3168'
    try:
        t3169 = merge_f(t3131)
    except:
        t3169 = None
    try:
        t3170 = lbind(prapply, manhattan)
    except:
        t3170 = None
    try:
        t3171 = get_nth_t(t3133, L1)
    except:
        t3171 = None
    try:
        t3172 = fill(t2407, t264, t3134)
    except:
        t3172 = None
    try:
        t3173 = lbind(contained, THREE)
    except:
        t3173 = None
    try:
        t3174 = combine_f(t3054, t3138)
    except:
        t3174 = None
    try:
        t3175 = paint(t700, t3139)
    except:
        t3175 = None
    if t3175 == O:
        return True, f'e6721834 - t3175'
    try:
        t3176 = toobject(t3140, t3098)
    except:
        t3176 = None
    try:
        t3177 = lbind(compose, t3142)
    except:
        t3177 = None
    try:
        t3178 = fill(t2696, BLACK, t3143)
    except:
        t3178 = None
    if t3178 == O:
        return True, f'3befdf3e - t3178'
    try:
        t3179 = mapply(t2780, t3144)
    except:
        t3179 = None
    try:
        t3180 = fork(shift, t368, t3146)
    except:
        t3180 = None
    try:
        t3181 = rbind(shift, t3147)
    except:
        t3181 = None
    try:
        t3182 = shift(t3148, ZERO_BY_TWO)
    except:
        t3182 = None
    try:
        t3183 = fill(I, t2444, t3149)
    except:
        t3183 = None
    try:
        t3184 = chain(t3110, t3150, dneighbors)
    except:
        t3184 = None
    try:
        t3185 = compose(t21, t2985)
    except:
        t3185 = None
    try:
        t3186 = identity(t138)
    except:
        t3186 = None
    try:
        t3187 = chain(increment, t23, t10)
    except:
        t3187 = None
    try:
        t3188 = mapply(t2352, t3152)
    except:
        t3188 = None
    try:
        t3189 = hupscale(t3153, THREE)
    except:
        t3189 = None
    if t3189 == O:
        return True, f'995c5fa3 - t3189'
    try:
        t3190 = shift(t2871, t3154)
    except:
        t3190 = None
    try:
        t3191 = fork(recolor_o, t804, t3155)
    except:
        t3191 = None
    try:
        t3192 = fill(t2731, CYAN, t3156)
    except:
        t3192 = None
    if t3192 == O:
        return True, f'9aec4887 - t3192'
    try:
        t3193 = paint(t242, t3157)
    except:
        t3193 = None
    if t3193 == O:
        return True, f'2bcee788 - t3193'
    try:
        t3194 = underfill(I, t807, t3158)
    except:
        t3194 = None
    if t3194 == O:
        return True, f'2bee17df - t3194'
    try:
        t3195 = apply(t298, t1227)
    except:
        t3195 = None
    try:
        t3196 = o_g(t3081, R7)
    except:
        t3196 = None
    try:
        t3197 = compose(asobject, t3160)
    except:
        t3197 = None
    try:
        t3198 = fork(recolor_o, t3161, identity)
    except:
        t3198 = None
    try:
        t3199 = combine(t2946, t3162)
    except:
        t3199 = None
    try:
        t3200 = lbind(fork, greater)
    except:
        t3200 = None
    try:
        t3201 = compose(t3085, t3164)
    except:
        t3201 = None
    try:
        t3202 = fill(I, t843, t3165)
    except:
        t3202 = None
    try:
        t3203 = mapply(t3045, t3167)
    except:
        t3203 = None
    try:
        t3204 = cover(t2894, t3169)
    except:
        t3204 = None
    try:
        t3205 = fork(t3170, identity, identity)
    except:
        t3205 = None
    try:
        t3206 = flip(t676)
    except:
        t3206 = None
    try:
        t3207 = mir_rot_t(t1672, R0)
    except:
        t3207 = None
    try:
        t3208 = t1091(t3173)
    except:
        t3208 = None
    try:
        t3209 = apply(t23, t3010)
    except:
        t3209 = None
    try:
        t3210 = fill(I, t2020, t3174)
    except:
        t3210 = None
    try:
        t3211 = f_ofcolor(t3098, FOUR)
    except:
        t3211 = None
    try:
        t3212 = compose(t3141, t298)
    except:
        t3212 = None
    try:
        t3213 = t3177(t2967)
    except:
        t3213 = None
    try:
        t3214 = paint(I, t3179)
    except:
        t3214 = None
    if t3214 == O:
        return True, f'447fd412 - t3214'
    try:
        t3215 = insert(t28, t2853)
    except:
        t3215 = None
    try:
        t3216 = fork(combine, t10, t3180)
    except:
        t3216 = None
    try:
        t3217 = rbind(f_ofcolor, FOUR)
    except:
        t3217 = None
    try:
        t3218 = astuple(ZERO, NEG_TWO)
    except:
        t3218 = None
    try:
        t3219 = branch(t1912, t2332, t2064)
    except:
        t3219 = None
    try:
        t3220 = matcher(t3184, RED)
    except:
        t3220 = None
    try:
        t3221 = lbind(apply, toivec)
    except:
        t3221 = None
    try:
        t3222 = c_zo_n(t84, t1, t3186)
    except:
        t3222 = None
    try:
        t3223 = fork(greater, t3187, t368)
    except:
        t3223 = None
    try:
        t3224 = underpaint(t861, t3188)
    except:
        t3224 = None
    if t3224 == O:
        return True, f'99fa7670 - t3224'
    try:
        t3225 = paint(t24, t3190)
    except:
        t3225 = None
    try:
        t3226 = apply(t3121, t3195)
    except:
        t3226 = None
    try:
        t3227 = color(t1967)
    except:
        t3227 = None
    try:
        t3228 = chain(color, merge, frontiers)
    except:
        t3228 = None
    try:
        t3229 = rbind(compose, t2947)
    except:
        t3229 = None
    try:
        t3230 = chain(size, t10, t2948)
    except:
        t3230 = None
    try:
        t3231 = replace(t3202, t251, BLACK)
    except:
        t3231 = None
    if t3231 == O:
        return True, f'a78176bb - t3231'
    try:
        t3232 = paint(t136, t3203)
    except:
        t3232 = None
    if t3232 == O:
        return True, f'a8c38be5 - t3232'
    try:
        t3233 = f_ofcolor(t3204, ONE)
    except:
        t3233 = None
    try:
        t3234 = compose(t3132, t3205)
    except:
        t3234 = None
    try:
        t3235 = branch(t3206, UNITY, DOWN_LEFT)
    except:
        t3235 = None
    try:
        t3236 = asobject(t3207)
    except:
        t3236 = None
    try:
        t3237 = fork(shift, identity, t3208)
    except:
        t3237 = None
    try:
        t3238 = apply(t2764, t3209)
    except:
        t3238 = None
    try:
        t3239 = get_nth_f(t3211, F0)
    except:
        t3239 = None
    try:
        t3240 = tojvec(NEG_TWO)
    except:
        t3240 = None
    try:
        t3241 = fork(shift, t3100, t3213)
    except:
        t3241 = None
    try:
        t3242 = insert(t1498, t3215)
    except:
        t3242 = None
    try:
        t3243 = fork(remove, t368, t23)
    except:
        t3243 = None
    try:
        t3244 = compose(t3181, t3217)
    except:
        t3244 = None
    try:
        t3245 = shift(t3148, t3218)
    except:
        t3245 = None
    try:
        t3246 = get_nth_f(t1562, L1)
    except:
        t3246 = None
    try:
        t3247 = sfilter_f(t3067, t3220)
    except:
        t3247 = None
    try:
        t3248 = get_arg_rank_f(t2986, t342, F0)
    except:
        t3248 = None
    try:
        t3249 = fork(both, t3151, t3223)
    except:
        t3249 = None
    try:
        t3250 = get_nth_f(t2558, F0)
    except:
        t3250 = None
    try:
        t3251 = colorfilter(t7, t2730)
    except:
        t3251 = None
    try:
        t3252 = mapply(t3037, t3226)
    except:
        t3252 = None
    try:
        t3253 = matcher(color, t3227)
    except:
        t3253 = None
    try:
        t3254 = fork(shift, t3197, t298)
    except:
        t3254 = None
    try:
        t3255 = t3228(I)
    except:
        t3255 = None
    try:
        t3256 = rbind(get_val_rank, L1)
    except:
        t3256 = None
    try:
        t3257 = compose(t3230, t1293)
    except:
        t3257 = None
    try:
        t3258 = initset(t2589)
    except:
        t3258 = None
    try:
        t3259 = chain(t3048, t1949, t3234)
    except:
        t3259 = None
    try:
        t3260 = multiply(t3235, t74)
    except:
        t3260 = None
    try:
        t3261 = lbind(shift, t3236)
    except:
        t3261 = None
    try:
        t3262 = chain(t61, t21, t3237)
    except:
        t3262 = None
    try:
        t3263 = papply(add, t3238, t3209)
    except:
        t3263 = None
    try:
        t3264 = rapply_f(t3137, t3102)
    except:
        t3264 = None
    try:
        t3265 = intersection(t181, t3174)
    except:
        t3265 = None
    try:
        t3266 = multiply(t3239, FOUR)
    except:
        t3266 = None
    try:
        t3267 = rbind(add, t3240)
    except:
        t3267 = None
    try:
        t3268 = t340(t3241)
    except:
        t3268 = None
    try:
        t3269 = fill(t3104, BLACK, t3242)
    except:
        t3269 = None
    try:
        t3270 = fork(astuple, t3216, t3243)
    except:
        t3270 = None
    try:
        t3271 = apply(t3244, t2203)
    except:
        t3271 = None
    try:
        t3272 = combine_f(t3182, t3245)
    except:
        t3272 = None
    try:
        t3273 = f_ofcolor(I, t3246)
    except:
        t3273 = None
    try:
        t3274 = rbind(adjacent, t219)
    except:
        t3274 = None
    try:
        t3275 = fill(t3112, t3222, t3248)
    except:
        t3275 = None
    if t3275 == O:
        return True, f'272f95fa - t3275'
    try:
        t3276 = lbind(compose, t3249)
    except:
        t3276 = None
    try:
        t3277 = shift(t3250, t2801)
    except:
        t3277 = None
    try:
        t3278 = mapply(t3191, t3251)
    except:
        t3278 = None
    try:
        t3279 = paint(I, t3252)
    except:
        t3279 = None
    if t3279 == O:
        return True, f'39e1d7f9 - t3279'
    try:
        t3280 = extract(t3196, t3253)
    except:
        t3280 = None
    try:
        t3281 = o_g(t268, R1)
    except:
        t3281 = None
    try:
        t3282 = lbind(contained, t3255)
    except:
        t3282 = None
    try:
        t3283 = rapply_t(t3199, t186)
    except:
        t3283 = None
    try:
        t3284 = lbind(lbind, t3256)
    except:
        t3284 = None
    try:
        t3285 = rbind(compose, t3257)
    except:
        t3285 = None
    try:
        t3286 = rbind(manhattan, t3258)
    except:
        t3286 = None
    try:
        t3287 = rbind(get_val_rank, F0)
    except:
        t3287 = None
    try:
        t3288 = double(t3260)
    except:
        t3288 = None
    try:
        t3289 = occurrences(t3172, t3236)
    except:
        t3289 = None
    try:
        t3290 = compose(t3173, palette_f)
    except:
        t3290 = None
    try:
        t3291 = papply(astuple, t3136, t3263)
    except:
        t3291 = None
    try:
        t3292 = mapply(t1684, t3264)
    except:
        t3292 = None
    try:
        t3293 = fill(t3210, t1861, t3265)
    except:
        t3293 = None
    if t3293 == O:
        return True, f'f1cefba8 - t3293'
    try:
        t3294 = shift(t3176, t3266)
    except:
        t3294 = None
    try:
        t3295 = fork(intersection, t2692, t3268)
    except:
        t3295 = None
    try:
        t3296 = branch(t2437, t3018, t3269)
    except:
        t3296 = None
    try:
        t3297 = apply(normalize, t3271)
    except:
        t3297 = None
    try:
        t3298 = paint(t2981, t3272)
    except:
        t3298 = None
    try:
        t3299 = intersection(t3273, t3108)
    except:
        t3299 = None
    try:
        t3300 = rbind(adjacent, t2633)
    except:
        t3300 = None
    try:
        t3301 = chain(decrement, t1949, shape_f)
    except:
        t3301 = None
    try:
        t3302 = double(t3073)
    except:
        t3302 = None
    try:
        t3303 = paint(I, t3278)
    except:
        t3303 = None
    try:
        t3304 = center(t3280)
    except:
        t3304 = None
    try:
        t3305 = mapply(t3254, t3281)
    except:
        t3305 = None
    try:
        t3306 = chain(t3282, palette_f, t3124)
    except:
        t3306 = None
    try:
        t3307 = mapply(t2381, t3283)
    except:
        t3307 = None
    try:
        t3308 = rbind(remove, t7)
    except:
        t3308 = None
    try:
        t3309 = compose(t3286, initset)
    except:
        t3309 = None
    try:
        t3310 = rbind(t3287, width_f)
    except:
        t3310 = None
    try:
        t3311 = add(t3171, t3288)
    except:
        t3311 = None
    try:
        t3312 = mapply(t3261, t3289)
    except:
        t3312 = None
    try:
        t3313 = sfilter_f(t2763, t3290)
    except:
        t3313 = None
    try:
        t3314 = mapply(t2686, t3291)
    except:
        t3314 = None
    try:
        t3315 = paint(I, t3292)
    except:
        t3315 = None
    if t3315 == O:
        return True, f'6aa20dc0 - t3315'
    try:
        t3316 = paint(t1690, t3294)
    except:
        t3316 = None
    if t3316 == O:
        return True, f'6d0160f0 - t3316'
    try:
        t3317 = fork(subtract, t1210, t3267)
    except:
        t3317 = None
    try:
        t3318 = chain(t67, t10, t3295)
    except:
        t3318 = None
    try:
        t3319 = t2323(t3296)
    except:
        t3319 = None
    if t3319 == O:
        return True, f'28e73c20 - t3319'
    try:
        t3320 = size_f(t17)
    except:
        t3320 = None
    try:
        t3321 = apply(t3106, t3297)
    except:
        t3321 = None
    try:
        t3322 = corner(t3272, R0)
    except:
        t3322 = None
    try:
        t3323 = fill(t3183, t3219, t3299)
    except:
        t3323 = None
    if t3323 == O:
        return True, f'd07ae81c - t3323'
    try:
        t3324 = fork(both, t3274, t3300)
    except:
        t3324 = None
    try:
        t3325 = compose(invert, t3301)
    except:
        t3325 = None
    try:
        t3326 = chain(t2930, t3276, t2885)
    except:
        t3326 = None
    try:
        t3327 = compose(t3267, t1210)
    except:
        t3327 = None
    try:
        t3328 = t2990(t3302)
    except:
        t3328 = None
    try:
        t3329 = subtract(t2119, t3304)
    except:
        t3329 = None
    try:
        t3330 = paint(t268, t3305)
    except:
        t3330 = None
    try:
        t3331 = compose(flip, t3306)
    except:
        t3331 = None
    try:
        t3332 = paint(I, t3307)
    except:
        t3332 = None
    if t3332 == O:
        return True, f'36d67576 - t3332'
    try:
        t3333 = chain(t3229, t3284, t3308)
    except:
        t3333 = None
    try:
        t3334 = get_arg_rank_f(t3233, t3309, F0)
    except:
        t3334 = None
    try:
        t3335 = compose(double, t3310)
    except:
        t3335 = None
    try:
        t3336 = subtract(t3171, t3288)
    except:
        t3336 = None
    try:
        t3337 = fill(t3172, RED, t3312)
    except:
        t3337 = None
    try:
        t3338 = get_arg_rank_f(t3313, size, F0)
    except:
        t3338 = None
    try:
        t3339 = underfill(I, t2604, t3314)
    except:
        t3339 = None
    if t3339 == O:
        return True, f'1e32b0e9 - t3339'
    try:
        t3340 = fork(shoot, t3267, t3317)
    except:
        t3340 = None
    try:
        t3341 = fork(recolor_o, t3318, t3241)
    except:
        t3341 = None
    try:
        t3342 = power(t3270, t3320)
    except:
        t3342 = None
    try:
        t3343 = matcher(size, ZERO)
    except:
        t3343 = None
    try:
        t3344 = corner(t3272, R1)
    except:
        t3344 = None
    try:
        t3345 = compose(t3324, initset)
    except:
        t3345 = None
    try:
        t3346 = compose(increment, t3301)
    except:
        t3346 = None
    try:
        t3347 = f_ofcolor(t2641, RED)
    except:
        t3347 = None
    try:
        t3348 = fork(connect, t3212, t3327)
    except:
        t3348 = None
    try:
        t3349 = shift(t3277, t3328)
    except:
        t3349 = None
    try:
        t3350 = lbind(rapply, t3199)
    except:
        t3350 = None
    try:
        t3351 = paint(t3303, t106)
    except:
        t3351 = None
    if t3351 == O:
        return True, f'57aa92db - t3351'
    try:
        t3352 = shift(t3159, t3329)
    except:
        t3352 = None
    try:
        t3353 = normalize(t108)
    except:
        t3353 = None
    try:
        t3354 = compose(numcolors_f, t3124)
    except:
        t3354 = None
    try:
        t3355 = compose(t2817, t1331)
    except:
        t3355 = None
    try:
        t3356 = chain(t3285, t708, t1570)
    except:
        t3356 = None
    try:
        t3357 = initset(t3334)
    except:
        t3357 = None
    try:
        t3358 = fork(add, t3259, t3335)
    except:
        t3358 = None
    try:
        t3359 = connect(t3311, t3336)
    except:
        t3359 = None
    try:
        t3360 = mir_rot_t(t1672, R1)
    except:
        t3360 = None
    try:
        t3361 = t3262(t3338)
    except:
        t3361 = None
    try:
        t3362 = fork(connect, t3212, t3340)
    except:
        t3362 = None
    try:
        t3363 = astuple(ZERO, DOWN_LEFT)
    except:
        t3363 = None
    try:
        t3364 = lbind(compose, t3343)
    except:
        t3364 = None
    try:
        t3365 = connect(t3322, t3344)
    except:
        t3365 = None
    try:
        t3366 = sfilter_f(t3247, t3345)
    except:
        t3366 = None
    try:
        t3367 = fork(t2440, t3325, t3346)
    except:
        t3367 = None
    try:
        t3368 = apply(t10, t3347)
    except:
        t3368 = None
    try:
        t3369 = chain(normalize, t3099, t3348)
    except:
        t3369 = None
    try:
        t3370 = paint(t3225, t3349)
    except:
        t3370 = None
    if t3370 == O:
        return True, f'f8a8fe49 - t3370'
    try:
        t3371 = paint(t2881, t3352)
    except:
        t3371 = None
    if t3371 == O:
        return True, f'4c5c2cf0 - t3371'
    try:
        t3372 = astuple(t826, t2998)
    except:
        t3372 = None
    try:
        t3373 = matcher(t3354, ONE)
    except:
        t3373 = None
    try:
        t3374 = fork(t3200, t3333, t3355)
    except:
        t3374 = None
    try:
        t3375 = fork(sfilter, t3201, t3356)
    except:
        t3375 = None
    try:
        t3376 = vline_i(t856)
    except:
        t3376 = None
    try:
        t3377 = fill(t2598, t807, t3359)
    except:
        t3377 = None
    try:
        t3378 = asobject(t3360)
    except:
        t3378 = None
    try:
        t3379 = remove_f(t3338, t3313)
    except:
        t3379 = None
    try:
        t3380 = chain(normalize, t3099, t3362)
    except:
        t3380 = None
    try:
        t3381 = mapply(t3341, t12)
    except:
        t3381 = None
    try:
        t3382 = initset(t3363)
    except:
        t3382 = None
    try:
        t3383 = lbind(rbind, difference)
    except:
        t3383 = None
    try:
        t3384 = shift(t3365, UP)
    except:
        t3384 = None
    try:
        t3385 = product(t3025, t3366)
    except:
        t3385 = None
    try:
        t3386 = compose(t3221, t3367)
    except:
        t3386 = None
    try:
        t3387 = insert(BLACK, t3368)
    except:
        t3387 = None
    try:
        t3388 = fork(shift, t3369, t3212)
    except:
        t3388 = None
    try:
        t3389 = rbind(greater, ONE)
    except:
        t3389 = None
    try:
        t3390 = add(UNITY, t3372)
    except:
        t3390 = None
    try:
        t3391 = fork(both, t3331, t3373)
    except:
        t3391 = None
    try:
        t3392 = compose(t117, t3374)
    except:
        t3392 = None
    try:
        t3393 = fork(apply, t2578, t3375)
    except:
        t3393 = None
    try:
        t3394 = center(t856)
    except:
        t3394 = None
    try:
        t3395 = paint(t3377, t157)
    except:
        t3395 = None
    try:
        t3396 = lbind(shift, t3378)
    except:
        t3396 = None
    try:
        t3397 = mapply(t3361, t3379)
    except:
        t3397 = None
    try:
        t3398 = fork(shift, t3380, t3212)
    except:
        t3398 = None
    try:
        t3399 = paint(I, t3381)
    except:
        t3399 = None
    try:
        t3400 = fill(t3298, t2785, t3384)
    except:
        t3400 = None
    try:
        t3401 = mapply(t2984, t3385)
    except:
        t3401 = None
    try:
        t3402 = fork(mapply, t3185, t3386)
    except:
        t3402 = None
    try:
        t3403 = order(t3387, identity)
    except:
        t3403 = None
    try:
        t3404 = fork(recolor_i, color, t3388)
    except:
        t3404 = None
    try:
        t3405 = compose(t3389, numcolors_f)
    except:
        t3405 = None
    try:
        t3406 = invert(t3390)
    except:
        t3406 = None
    try:
        t3407 = sfilter(t1808, t3391)
    except:
        t3407 = None
    try:
        t3408 = fork(intersection, t3163, t3392)
    except:
        t3408 = None
    try:
        t3409 = fork(mapply, t113, t3393)
    except:
        t3409 = None
    try:
        t3410 = shoot(t3394, DOWN)
    except:
        t3410 = None
    try:
        t3411 = compose(t823, color)
    except:
        t3411 = None
    try:
        t3412 = paint(t3395, t187)
    except:
        t3412 = None
    if t3412 == O:
        return True, f'508bd3b6 - t3412'
    try:
        t3413 = occurrences(t3337, t3378)
    except:
        t3413 = None
    try:
        t3414 = combine_f(t3135, t3397)
    except:
        t3414 = None
    try:
        t3415 = fork(recolor_i, color, t3398)
    except:
        t3415 = None
    try:
        t3416 = lbind(difference, t1863)
    except:
        t3416 = None
    try:
        t3417 = corner(t3272, R2)
    except:
        t3417 = None
    try:
        t3418 = fill(t2716, YELLOW, t3401)
    except:
        t3418 = None
    if t3418 == O:
        return True, f'aba27056 - t3418'
    try:
        t3419 = compose(vline_i, t2985)
    except:
        t3419 = None
    try:
        t3420 = height_t(t2641)
    except:
        t3420 = None
    try:
        t3421 = mapply(t3404, t2612)
    except:
        t3421 = None
    try:
        t3422 = sfilter(t17, t3405)
    except:
        t3422 = None
    try:
        t3423 = shift(t3353, t3406)
    except:
        t3423 = None
    try:
        t3424 = mapply(t3198, t3407)
    except:
        t3424 = None
    try:
        t3425 = fork(recolor_i, color, t3408)
    except:
        t3425 = None
    try:
        t3426 = shoot(t3394, UP)
    except:
        t3426 = None
    try:
        t3427 = compose(t3358, t3411)
    except:
        t3427 = None
    try:
        t3428 = mapply(t3396, t3413)
    except:
        t3428 = None
    try:
        t3429 = paint(I, t3414)
    except:
        t3429 = None
    if t3429 == O:
        return True, f'3e980e27 - t3429'
    try:
        t3430 = mapply(t3415, t2609)
    except:
        t3430 = None
    try:
        t3431 = mapply(t3415, t2612)
    except:
        t3431 = None
    try:
        t3432 = apply(t3416, t3271)
    except:
        t3432 = None
    try:
        t3433 = corner(t3272, R3)
    except:
        t3433 = None
    try:
        t3434 = sfilter_f(t17, t3419)
    except:
        t3434 = None
    try:
        t3435 = insert(t3420, t3368)
    except:
        t3435 = None
    try:
        t3436 = paint(t2969, t3421)
    except:
        t3436 = None
    try:
        t3437 = mapply(t3350, t3422)
    except:
        t3437 = None
    try:
        t3438 = lbind(shift, t3423)
    except:
        t3438 = None
    try:
        t3439 = paint(t1235, t3424)
    except:
        t3439 = None
    try:
        t3440 = mapply(t3425, t7)
    except:
        t3440 = None
    try:
        t3441 = combine(t3410, t3426)
    except:
        t3441 = None
    try:
        t3442 = compose(invert, t3427)
    except:
        t3442 = None
    try:
        t3443 = fill(t3337, RED, t3428)
    except:
        t3443 = None
    try:
        t3444 = paint(t2966, t3430)
    except:
        t3444 = None
    try:
        t3445 = chain(tojvec, t23, t2907)
    except:
        t3445 = None
    try:
        t3446 = paint(t2969, t3431)
    except:
        t3446 = None
    try:
        t3447 = apply(t3383, t3432)
    except:
        t3447 = None
    try:
        t3448 = connect(t3417, t3433)
    except:
        t3448 = None
    try:
        t3449 = difference(t17, t3434)
    except:
        t3449 = None
    try:
        t3450 = apply(decrement, t3435)
    except:
        t3450 = None
    try:
        t3451 = mir_rot_t(t3436, R4)
    except:
        t3451 = None
    try:
        t3452 = mapply(t2803, t3437)
    except:
        t3452 = None
    try:
        t3453 = occurrences(t268, t2377)
    except:
        t3453 = None
    try:
        t3454 = t3040(t3439)
    except:
        t3454 = None
    try:
        t3455 = paint(I, t3440)
    except:
        t3455 = None
    if t3455 == O:
        return True, f'd22278a0 - t3455'
    try:
        t3456 = shoot(t3394, LEFT)
    except:
        t3456 = None
    try:
        t3457 = order(t20, t3442)
    except:
        t3457 = None
    try:
        t3458 = mir_rot_t(t3360, R2)
    except:
        t3458 = None
    try:
        t3459 = mir_rot_t(t3444, R4)
    except:
        t3459 = None
    try:
        t3460 = fork(multiply, shape_f, t3445)
    except:
        t3460 = None
    try:
        t3461 = mir_rot_t(t3446, R4)
    except:
        t3461 = None
    try:
        t3462 = c_iz_n(t84, t1, t603)
    except:
        t3462 = None
    try:
        t3463 = apply(t21, t3297)
    except:
        t3463 = None
    try:
        t3464 = shift(t3448, DOWN)
    except:
        t3464 = None
    try:
        t3465 = mapply(t3402, t3449)
    except:
        t3465 = None
    try:
        t3466 = order(t3450, identity)
    except:
        t3466 = None
    try:
        t3467 = papply(pair, t3436, t3451)
    except:
        t3467 = None
    try:
        t3468 = paint(I, t3452)
    except:
        t3468 = None
    try:
        t3469 = mapply(t3438, t3453)
    except:
        t3469 = None
    try:
        t3470 = downscale(t3454, t2124)
    except:
        t3470 = None
    if t3470 == O:
        return True, f'7837ac64 - t3470'
    try:
        t3471 = shoot(t3394, RIGHT)
    except:
        t3471 = None
    try:
        t3472 = apply(t2956, t3457)
    except:
        t3472 = None
    try:
        t3473 = asobject(t3458)
    except:
        t3473 = None
    try:
        t3474 = papply(pair, t3444, t3459)
    except:
        t3474 = None
    try:
        t3475 = fork(shift, t689, t3460)
    except:
        t3475 = None
    try:
        t3476 = papply(pair, t3446, t3461)
    except:
        t3476 = None
    try:
        t3477 = rbind(other, t3462)
    except:
        t3477 = None
    try:
        t3478 = papply(compose, t3447, t3463)
    except:
        t3478 = None
    try:
        t3479 = fill(t3400, t1907, t3464)
    except:
        t3479 = None
    try:
        t3480 = lbind(apply, tojvec)
    except:
        t3480 = None
    try:
        t3481 = pair(t3403, t3466)
    except:
        t3481 = None
    try:
        t3482 = apply(t175, t3467)
    except:
        t3482 = None
    try:
        t3483 = merge_f(t3422)
    except:
        t3483 = None
    try:
        t3484 = paint(t3330, t3469)
    except:
        t3484 = None
    try:
        t3485 = combine(t3456, t3471)
    except:
        t3485 = None
    try:
        t3486 = apply(normalize, t3472)
    except:
        t3486 = None
    try:
        t3487 = lbind(shift, t3473)
    except:
        t3487 = None
    try:
        t3488 = apply(t175, t3474)
    except:
        t3488 = None
    try:
        t3489 = t2769(t3475)
    except:
        t3489 = None
    try:
        t3490 = apply(t175, t3476)
    except:
        t3490 = None
    try:
        t3491 = compose(t3477, palette_f)
    except:
        t3491 = None
    try:
        t3492 = apply(t3364, t3478)
    except:
        t3492 = None
    try:
        t3493 = cover(t3479, t3107)
    except:
        t3493 = None
    try:
        t3494 = compose(t3480, t3367)
    except:
        t3494 = None
    try:
        t3495 = apply(t3326, t3481)
    except:
        t3495 = None
    try:
        t3496 = mir_rot_t(t3436, R5)
    except:
        t3496 = None
    try:
        t3497 = cover(t3468, t3483)
    except:
        t3497 = None
    if t3497 == O:
        return True, f'0e206a2e - t3497'
    try:
        t3498 = get_color_rank_t(t268, F0)
    except:
        t3498 = None
    try:
        t3499 = branch(t3376, t3441, t3485)
    except:
        t3499 = None
    try:
        t3500 = interval(ZERO, t1066, ONE)
    except:
        t3500 = None
    try:
        t3501 = occurrences(t3443, t3473)
    except:
        t3501 = None
    try:
        t3502 = mir_rot_t(t3444, R5)
    except:
        t3502 = None
    try:
        t3503 = t3177(t3445)
    except:
        t3503 = None
    try:
        t3504 = mir_rot_t(t3446, R5)
    except:
        t3504 = None
    try:
        t3505 = fork(recolor_o, t3491, identity)
    except:
        t3505 = None
    try:
        t3506 = papply(sfilter, t3321, t3492)
    except:
        t3506 = None
    try:
        t3507 = t749(t3493)
    except:
        t3507 = None
    if t3507 == O:
        return True, f'b7249182 - t3507'
    try:
        t3508 = fork(mapply, t3185, t3494)
    except:
        t3508 = None
    try:
        t3509 = size_f(t3347)
    except:
        t3509 = None
    try:
        t3510 = papply(pair, t3482, t3496)
    except:
        t3510 = None
    try:
        t3511 = f_ofcolor(t268, t3498)
    except:
        t3511 = None
    try:
        t3512 = gravitate(t3357, t3499)
    except:
        t3512 = None
    try:
        t3513 = pair(t3500, t3500)
    except:
        t3513 = None
    try:
        t3514 = mapply(t3487, t3501)
    except:
        t3514 = None
    try:
        t3515 = papply(pair, t3488, t3502)
    except:
        t3515 = None
    try:
        t3516 = fork(shift, t3489, t3503)
    except:
        t3516 = None
    try:
        t3517 = papply(pair, t3490, t3504)
    except:
        t3517 = None
    try:
        t3518 = apply(t3505, t17)
    except:
        t3518 = None
    try:
        t3519 = mpapply(mapply, t2326, t3506)
    except:
        t3519 = None
    try:
        t3520 = mapply(t3508, t3434)
    except:
        t3520 = None
    try:
        t3521 = increment(t3509)
    except:
        t3521 = None
    try:
        t3522 = apply(t175, t3510)
    except:
        t3522 = None
    try:
        t3523 = fill(t3484, t3498, t3511)
    except:
        t3523 = None
    if t3523 == O:
        return True, f'264363fd - t3523'
    try:
        t3524 = crement(t3512)
    except:
        t3524 = None
    try:
        t3525 = mpapply(shift, t3486, t3513)
    except:
        t3525 = None
    try:
        t3526 = fill(t3443, t264, t3514)
    except:
        t3526 = None
    if t3526 == O:
        return True, f'150deff5 - t3526'
    try:
        t3527 = apply(t175, t3515)
    except:
        t3527 = None
    try:
        t3528 = t340(t3516)
    except:
        t3528 = None
    try:
        t3529 = apply(t175, t3517)
    except:
        t3529 = None
    try:
        t3530 = order(t3518, t342)
    except:
        t3530 = None
    try:
        t3531 = fill(I, ONE, t3519)
    except:
        t3531 = None
    if t3531 == O:
        return True, f'7df24a62 - t3531'
    try:
        t3532 = combine_f(t3465, t3520)
    except:
        t3532 = None
    try:
        t3533 = interval(ZERO, t3521, ONE)
    except:
        t3533 = None
    try:
        t3534 = mir_rot_t(t3436, R6)
    except:
        t3534 = None
    try:
        t3535 = add(t3334, t3524)
    except:
        t3535 = None
    try:
        t3536 = paint(t1836, t3525)
    except:
        t3536 = None
    try:
        t3537 = mir_rot_t(t3444, R6)
    except:
        t3537 = None
    try:
        t3538 = fork(intersection, t2692, t3528)
    except:
        t3538 = None
    try:
        t3539 = mir_rot_t(t3446, R6)
    except:
        t3539 = None
    try:
        t3540 = astuple(t3382, t3530)
    except:
        t3540 = None
    try:
        t3541 = underfill(t3111, THREE, t3532)
    except:
        t3541 = None
    if t3541 == O:
        return True, f'b527c5c6 - t3541'
    try:
        t3542 = apply(tojvec, t3533)
    except:
        t3542 = None
    try:
        t3543 = papply(pair, t3522, t3534)
    except:
        t3543 = None
    try:
        t3544 = connect(t3334, t3535)
    except:
        t3544 = None
    try:
        t3545 = mir_rot_t(t3536, R4)
    except:
        t3545 = None
    try:
        t3546 = papply(pair, t3527, t3537)
    except:
        t3546 = None
    try:
        t3547 = chain(t67, t10, t3538)
    except:
        t3547 = None
    try:
        t3548 = papply(pair, t3529, t3539)
    except:
        t3548 = None
    try:
        t3549 = t3342(t3540)
    except:
        t3549 = None
    try:
        t3550 = papply(shift, t3495, t3542)
    except:
        t3550 = None
    try:
        t3551 = apply(t175, t3543)
    except:
        t3551 = None
    if t3551 == O:
        return True, f'9d9215db - t3551'
    try:
        t3552 = fill(t3204, ONE, t3544)
    except:
        t3552 = None
    try:
        t3553 = paint(t3545, t3525)
    except:
        t3553 = None
    try:
        t3554 = apply(t175, t3546)
    except:
        t3554 = None
    if t3554 == O:
        return True, f'9ddd00f0 - t3554'
    try:
        t3555 = fork(recolor_o, t3547, t3516)
    except:
        t3555 = None
    try:
        t3556 = apply(t175, t3548)
    except:
        t3556 = None
    if t3556 == O:
        return True, f'5751f35e - t3556'
    try:
        t3557 = get_nth_f(t3549, F0)
    except:
        t3557 = None
    try:
        t3558 = merge(t3550)
    except:
        t3558 = None
    try:
        t3559 = lbind(rapply, t3125)
    except:
        t3559 = None
    try:
        t3560 = connect(t3535, t3394)
    except:
        t3560 = None
    try:
        t3561 = mir_rot_t(t3553, R4)
    except:
        t3561 = None
    try:
        t3562 = mapply(t3555, t12)
    except:
        t3562 = None
    try:
        t3563 = width_f(t3557)
    except:
        t3563 = None
    try:
        t3564 = fill(t2641, CYAN, t3558)
    except:
        t3564 = None
    try:
        t3565 = underfill(t3552, ONE, t3560)
    except:
        t3565 = None
    try:
        t3566 = paint(t3561, t3525)
    except:
        t3566 = None
    try:
        t3567 = paint(t3399, t3562)
    except:
        t3567 = None
    try:
        t3568 = decrement(t3563)
    except:
        t3568 = None
    try:
        t3569 = t2554(t3564)
    except:
        t3569 = None
    if t3569 == O:
        return True, f'f15e1fac - t3569'
    try:
        t3570 = compose(t897, numcolors_f)
    except:
        t3570 = None
    try:
        t3571 = replace(t3565, ONE, THREE)
    except:
        t3571 = None
    if t3571 == O:
        return True, f'2dd70a9a - t3571'
    try:
        t3572 = mir_rot_t(t3566, R4)
    except:
        t3572 = None
    try:
        t3573 = compose(t2286, t689)
    except:
        t3573 = None
    try:
        t3574 = astuple(THREE, t3568)
    except:
        t3574 = None
    try:
        t3575 = sfilter_f(t12, t3570)
    except:
        t3575 = None
    try:
        t3576 = paint(t3572, t3525)
    except:
        t3576 = None
    if t3576 == O:
        return True, f'4290ef0e - t3576'
    try:
        t3577 = fork(multiply, shape_f, t2907)
    except:
        t3577 = None
    try:
        t3578 = canvas(BLACK, t3574)
    except:
        t3578 = None
    try:
        t3579 = mapply(t3559, t3575)
    except:
        t3579 = None
    try:
        t3580 = fork(shift, t3573, t3577)
    except:
        t3580 = None
    try:
        t3581 = paint(t3578, t3557)
    except:
        t3581 = None
    if t3581 == O:
        return True, f'234bbc79 - t3581'
    if t3581 == O:
        return True, f'd017b73f - t3581'
    try:
        t3582 = mapply(t3409, t3579)
    except:
        t3582 = None
    try:
        t3583 = t2769(t3580)
    except:
        t3583 = None
    try:
        t3584 = paint(t282, t3582)
    except:
        t3584 = None
    try:
        t3585 = t3177(t2907)
    except:
        t3585 = None
    try:
        t3586 = fork(apply, t2578, t3164)
    except:
        t3586 = None
    try:
        t3587 = fork(shift, t3583, t3585)
    except:
        t3587 = None
    try:
        t3588 = fork(mapply, t113, t3586)
    except:
        t3588 = None
    try:
        t3589 = t340(t3587)
    except:
        t3589 = None
    try:
        t3590 = lbind(remove, RED)
    except:
        t3590 = None
    try:
        t3591 = fork(intersection, t2692, t3589)
    except:
        t3591 = None
    try:
        t3592 = palette_t(t3582)
    except:
        t3592 = None
    try:
        t3593 = chain(t67, t10, t3591)
    except:
        t3593 = None
    try:
        t3594 = t3590(t3592)
    except:
        t3594 = None
    try:
        t3595 = fork(recolor_o, t3593, t3587)
    except:
        t3595 = None
    try:
        t3596 = rbind(contained, t3594)
    except:
        t3596 = None
    try:
        t3597 = mapply(t3595, t12)
    except:
        t3597 = None
    try:
        t3598 = chain(t10, t3590, palette_f)
    except:
        t3598 = None
    try:
        t3599 = paint(t3567, t3597)
    except:
        t3599 = None
    if t3599 == O:
        return True, f'b775ac94 - t3599'
    try:
        t3600 = chain(flip, t3596, t3598)
    except:
        t3600 = None
    try:
        t3601 = sfilter_f(t3575, t3600)
    except:
        t3601 = None
    try:
        t3602 = mapply(t3559, t3601)
    except:
        t3602 = None
    try:
        t3603 = mapply(t3588, t3602)
    except:
        t3603 = None
    try:
        t3604 = paint(t3584, t3603)
    except:
        t3604 = None
    if t3604 == O:
        return True, f'97a05b5b - t3604'
    return False, None

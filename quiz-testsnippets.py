# --- QUIZ -- Test-Code ---


def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    power = base ** exp 
    while power < num:
        exp += 1
    if power > num:
        hi = exp
        lo = exp - 1
    elif power == num:
        hi = exp + 1
        lo = exp - 1
    epsilon_lo = abs(num-lo)
    epsilon_hi = abs(hi - num)
    if epsilon_lo > epsilon_hi:
        return hi
    elif epsilon_lo <= epsilon_hi:
        return lo

    # Your code here:
#   For example,
#   closest_power(3,12) returns 2
#   closest_power(4,12) returns 2
#   closest_power(4,1) returns 0
#   "Finde den Exponenten(= Funct-Return!) der Basis 'base' der
#   am nähesten an der Integer-Zahl "num" dran ist "
#   base ** x < num, base ** x > num NOT base ** x == num !!!
#   If tie - return the smaller value!

#   Initialize Variable: exp = 0 (Exponent of base)
#   start calculating base ** exp (=power) (exp=0, exp++)- increment exp +1 per iteration
#   If base ** exp > num: lo=exp-1; hi=exp
#   If base ** exp == num: lo=exp-1; hi=exp+1
#   epsilon_lo = abs(num-lo) OR epsilon_hi=abs(hi-num)
#   if epsilon_lo > epsilon_hi: closest=hi 
#   elif epsilon_lo < epsilon_hi: closest=lo
#   elif epsilon_lo == epsilon_hi: closest=lo

closest_power(3,12)
closest_power(4,12)
closest_power(4,1)
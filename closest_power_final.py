def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    base = int(base)
    num = int(num)
    exp = 0
    power = 0
    while power < num:
        exp += 1
        power = base ** exp
        # print("power:", power, "exp:", exp, "num:", num)    
    if power == num:
        # print("closest power of base: ", base, "to num: ", num, "is: ", exp)
        return exp
    else:
        lo = base ** (exp - 1)
        hi = power
    if (abs(num - lo)) > (abs(hi - num)):
        # print("closest power of base: ", base, "to num: ", num, "is: ", exp)
        return exp 
    elif (abs(num - lo)) < (abs(hi - num)):
        # print("closest power of base: ", base, "to num: ", num, "is: ", (exp-1))
        return exp - 1
    elif (abs(num - lo)) == (abs(hi - num)):
        return exp - 1

# ----- Account for Floats !!! ---- DONE
# ----- Acount for eps-hi == eps-lo !!! ---- DONE

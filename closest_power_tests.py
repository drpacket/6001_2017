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
        print("power:", power, "exp:", exp, "base:", base, "num:", num)    
    if power == num:
        print("closest power of base: ", base, "to num: ", num, "is: ", exp)
        return exp
    else:
        lo = base ** (exp - 1)
        hi = power
    if (abs(num - lo)) > (abs(hi - num)):
        print("closest power of base: ", base, "to num: ", num, "is: ", exp)
        return exp 
    elif (abs(num - lo)) < (abs(hi - num)):
        print("closest power of base: ", base, "to num: ", num, "is: ", (exp-1))
        return exp - 1
    elif (abs(num - lo)) == (abs(hi - num)):
        return exp - 1
print("---------------------------------------------------")

print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))

print("---------------------------------------------------")

print(closest_power(5,20))
print(closest_power(6,36))
print(closest_power(2,1))

print("---------------------------------------------------")

print(closest_power(5,25))
print(closest_power(3,27))
print(closest_power(2,16))
print(closest_power(4,64))

print("---------------------------------------------------")

print(closest_power(2, 192))
print(closest_power(5, 375))
print(closest_power(20, 210))

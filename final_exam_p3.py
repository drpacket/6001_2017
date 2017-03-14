# ---------------------------------------------------------------------------- #
# -------- *** MITx course 600.1x ** Online course on edx *** ---------------- #
# ------- Introduction to Computer Science and Programming using Python ------ #
# ---------------------- [Final Exam - Problem 3] ---------------------------- #
# ---------------------------------------------------------------------------- #

# Problem 3
# 10.0 points possible (graded)
# ---------------------------------------------------------------------------- #

# ---> Numbers in Mandarin follow 3 simple rules:

# There are words for each of the digits from 0 to 10.
# For numbers 11-19, the number is pronounced as "ten digit",
# for example, 16 would be pronounced (using Mandarin) as "ten six".

# For numbers between 20 and 99, the number is pronounced as “digit ten digit”,
# for example, 37 would be pronounced (using Mandarin) as "three ten seven".
# If the digit is a zero, it is not included.

# Example Usage:

# convert_to_mandarin('36') will return san shi liu
# convert_to_mandarin('20') will return er shi
# convert_to_mandarin('16') will return shi liu

# ---> We want to write a procedure that converts an American number (between 0 and 99),
# written as a string, into the equivalent Mandarin.

# Paste your entire function, including the definition, in the box below.
# Assume that we provide 'trans' for you. Do not leave any debugging print statements.

# ---------------------------------------------------------------------------- #

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

# def convert_to_mandarin(us_num):
#     '''
#     us_num, a string representing a US number 0 to 99
#     returns the string mandarin representation of us_num
#     '''
    # FILL IN YOUR CODE HERE

# ---------------------------------------------------------------------------- #

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    us_num = int(us_num)
    if us_num <= 10:
        answer = trans[str(us_num)]
    elif us_num <= 19:
        answer = "shi " + trans[str(us_num - 10)]
    else:
        if us_num % 10 == 0:
            us_num = str(us_num)
            answer = trans[us_num[0]] + " shi"
        else:
            us_num = str(us_num)
            answer = trans[us_num[0]] + " shi " + trans[us_num[1]]
    return answer


print(convert_to_mandarin(36))
print(convert_to_mandarin(20))
print(convert_to_mandarin(16))

print(convert_to_mandarin(0))

print(convert_to_mandarin(99))

print(convert_to_mandarin(40))
print(convert_to_mandarin(60))
print(convert_to_mandarin(80))



# *** EOF ***
# ---------------------------------------------------------------------------- #
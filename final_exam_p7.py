# ---------------------------------------------------------------------------- #
# -------- *** MITx course 600.1x ** Online course on edx *** ---------------- #
# ------- Introduction to Computer Science and Programming using Python ------ #
# ---------------------- [Final Exam - Problem 7] ---------------------------- #
# ---------------------------------------------------------------------------- #

# Problem 7
# 20.0 points possible (graded)
# ---------------------------------------------------------------------------- #

# ---> Write a function called general_poly, that meets the specifications below:


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def to_apply (x):
        n = 0
        for i in L:
            n = x*n + i
        return n
    return to_apply


# *** EOF ***
# ---------------------------------------------------------------------------- #
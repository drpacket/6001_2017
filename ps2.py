# ---------------------------------------------------------------------------- # 
# -------- *** MITx course 600.1x ** Online course on edx *** ---------------- #
# ------- Introduction to Computer Science and Programming using Python ------ #
# ----------------------- [Problem Set #2] ----------------------------------- #
# ---------------------------------------------------------------------------- #

# *** Problem 1: Credit Card Balance after a Year. Minimum Monthly Payment ***
# ---------------------------------------------------------------------------- #

MONTHS = 12.0
totalPaid = 0

for month in range(1,13):
    minPayment = balance * monthlyPaymentRate
    unpaid = balance - minPayment
    interest = (annualInterestRate/MONTHS) * unpaid
    balance = unpaid + interest
    totalPaid += minPayment
    

print("Remaining balance: %0.2f" % balance)

# *** Problem 2: Paying Debt Off in a Year. Minimum Monthly Payment Amount ***
# ---------------------------------------------------------------------------- #

remaining = 1
minPay = 0

while remaining > 0 :
    remaining = balance
    minPay += 10
    for month in range(1,13):
            unpaid = remaining - minPay
            interest = (annualInterestRate/12.0) * unpaid
            remaining = unpaid + interest
print('Lowest Payment: %d' % minPay)

# *** Problem 3: Using Bisection Search to Make the Program Faster ***
# ---------------------------------------------------------------------------- #

hi = (balance*(1+(annualInterestRate/12.0))**12)/12.0
lo = balance/12.0
guessed = False
remaining = 0

while not guessed:
    remaining = balance
    guess = (hi + lo)/2
    for month in range(1,13):
            unpaid = remaining - guess
            interest = (annualInterestRate/12.0) * unpaid
            remaining = unpaid + interest
    if remaining < 0.0:
        hi = guess
    elif remaining > 0.0:
        lo = guess
    if remaining > -0.01 and remaining < 0.01:
        guessed = True

print('Lowest Payment: %0.2f' % guess)

# *** EOF ***
# ---------------------------------------------------------------------------- #
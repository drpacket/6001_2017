# ---------------------------------------------------------------------------- # 
# ------- *** MITx course 600.1x --- Online course on edx *** ---------------- #
# ------> Introduction to Computer Science and Programming using Python <----- #
# -------------------- *** Finger Exercise *** ------------------------------- #
# ---------------------------------------------------------------------------- #

import random

high = 100
low = 0

def guess_number(high, low):
    guessed = (high + low) // 2
    return guessed

print("Please think of a number between 0 and 100!")

while True:
    guessed = guess_number(high, low)
    print("Is your secret number " + str(guessed) + "?")
    choice = input("Enter 'h' to indicate the guess is too high. Enter 'l' to \
indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    choice = choice.lower()
    if choice == "h":
        high = guessed
    elif choice == "l":
        low = guessed
    elif choice == "c":
        break
    else:
        print("Invalid Input")
        continue

print("Game over. Your secret number was: " + str(guessed))

# *** EOF ***
# ---------------------------------------------------------------------------- #
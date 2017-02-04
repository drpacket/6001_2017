# ---------------------------------------------------------------------------- # 
# ------- *** MITx course 600.1x --- Online course on edx *** ---------------- #
# ------> Introduction to Computer Science and Programming using Python <----- #
# -------------------- *** Finger Exercise *** ------------------------------- #
# ---------------------------------------------------------------------------- #

# Exercise: guess my number *** Note: This is private, extended Version ***
# *** See separate file for regular Version! ***
# 10.0 points possible (graded)
# ESTIMATED TIME TO COMPLETE: 15 minutes

# In this problem, you'll create a program that guesses a secret number!
# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low?
# Using bisection search, the computer will guess the user's secret number!
 
# Note: your program should use input to obtain the user's input!
# Be sure to handle the case when the user's input is not one of h, l, or c.
# When the user enters something invalid, you should print out a message to the user
# explaining you did not understand their input.
# Then, you should re-ask the question, and prompt again for input.

import random

print('\nWelcome to the Game "Computer finds guessed Number".\nThink of a Number between \
0 and 99 ...')

high = 100
low = 0
no_guesses = 1
# guessed = random.randint(low, high) # possibly better/correct instead?

def guess_number(high, low):
    guessed = (high + low) // 2
    return guessed

while True:
    guessed = guess_number(high, low)
    print("\n-----------------------------------------------------")
    print("Is your number " + str(guessed) + " ? (** Guess #" + str(no_guesses) + " **)")
    print("-----------------------------------------------------")
    no_guesses += 1
    choice = input("Enter 'h' to indicate the guess is too high.\n\
Enter 'l' to indicate the guess is too low. \nEnter 'c' to indicate I guessed correctly.\n>> ")
    choice = choice.lower()

    if choice == "h":
        high = guessed
    elif choice == "l":
        low = guessed
    elif choice == "c":
        print("\nSeems like I guessed your number! ")
        print("-----------------------------------------------------")
        print("--- Your number was: " + str(guessed) + " --- Number of Guesses:", no_guesses, "----")
        print("-----------------------------------------------------\n")
        break
    else:
        print("Invalid Input!\n")
        continue

# *** EOF ***
# ---------------------------------------------------------------------------- #
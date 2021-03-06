# --- MITx 600.1x -- Problem Set 1 ---
# Problem Set 1 due Jan 27, 2017 00:30 CET

# -- Problem 1 (10 Points) -- 
# 10.0 points possible (graded)

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

# - Problem Set 1 due Jan 27, 2017 00:30 CET -
# Paste your code into this box:

s = "a.wet,h,u,oeeee,caa,eii,*usfjleiioefkjsfkshdfe$u"

def is_vowel(letter):
    if letter.lower() in "aeiou":
        return True
    else:
        return False
    
def vowels_in_string(s):
    total = 0
    for letter in s:
        if is_vowel(letter):
            total += 1
    return total

print(vowels_in_string(s))


# -- Problem 2 (10 Points) --
# 10.0 points possible (graded)

# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print:
# Number of times bob occurs is: 2

# - Problem Set 1 due Jan 27, 2017 00:30 CET -
# Paste your code into this box:

# Example String s
s = 'azcbobobegghabobmsdfsjhsdfbosdfsdfbobkldfjbdfgobesshbobsdfjjf' 

# Function to "count_bob" - return #Occurances of substring "bob" in s
def count_bob(s):
    count = 0
    for i in range(len(s)):
        if s[i:(i+3)] == "bob":
            count += 1
    return count

print(count_bob(s))


# -- Problem 3 (15 Points) --
# 15.0 points possible (graded)

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s 
# in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart.
# If you've spent more than a few hours on this problem, we suggest that 
# you move on to a different part of the course.
# If you have time, come back to this problem
# after you've had a break and cleared your head.

# - Problem Set 1 due Jan 27, 2017 00:30 CET -
# Paste your code into this box:

maxLen = 0
sub = s[0]
longest = s[0]

for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        sub += s[i + 1]
        if len(sub) > maxLen:
            maxLen = len(sub)
            longest = sub
    else:
        sub = s[i + 1]
        
    i += 1

print ('Longest substring in alphabetical order in string s:', longest)

# --- --- --- --- --- --- --- --- --- --- --- ---
# alpha = "abcdefghijklmnopqrstuvwxyz"
# sub = ""
# 
# for i in range(len(s)):
#     print(i, s[i])
#     for j in range(len(alpha)):
#         print(j, alpha[j])
#         if s[i] == alpha[j]:
#             sub += s[i]
#             print(sub)
#             break
#     longest = sub
#     print(longest)
#     sub = ""


# sub = []
# i = 0
# while s[i].isalpha():
#     sub.append(s[i])
#     i += 1


# --- Possibly useful String-Methods ---:
# index(...)
#  |      S.index(sub[, start[, end]]) -> int
#  |
#  |      Like S.find() but raise ValueError when the substring is not found.
# --- --- --- --- --- --- --- --- --- --- 
# isalpha(...)
#  |      S.isalpha() -> bool
#  |
#  |      Return True if all characters in S are alphabetic
#  |      and there is at least one character in S, False otherwise.
# --- --- --- --- --- --- --- --- --- --- 
# rfind(...)
#  |      S.rfind(sub[, start[, end]]) -> int
#  |
#  |      Return the highest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |
#  |      Return -1 on failure.#




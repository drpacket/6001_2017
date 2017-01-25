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

# Paste your code into this box:

s = "ktfdguhsf33uhfsu3.gdk.fjddefg"

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
# OLD WORK-CODE:

# for i in range(len(s)):
#     counter = 0
#     while s[i]

# - Problem Set 1 due Jan 27, 2017 00:30 CET -

# s = "ktfdguhsf33uhfsu3.gdk.fjddefg"
# 
# alpha = "abcdefghijklmnopqrstuvwxyz"
# sub = ""
# longest = ""
# iterate = 0
# for i in range(len(s)):
#     for j in range(len(alpha)):
#         if s[i] == alpha[j]:   
#             sub += s[i]
#             print
#             if len(sub) > len(longest):
#                 longest = sub
#         iterate += 1
#         print("sub =", sub)
#         print("longest =", longest)
#         print("iteration:", iterate)


# sub = []
# i = 0
# while s[i].isalpha():
#     sub.append(s[i])
#     i += 1

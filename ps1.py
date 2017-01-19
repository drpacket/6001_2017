# Problem Set 1
# 10.0 points possible (graded)
# Assume s is a string of lower case characters.
 
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

# Problem Set 1 due Jan 27, 2017 00:30 CET

s = "a.wet,h,u,oeeee,caa,eii,*u$u"

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





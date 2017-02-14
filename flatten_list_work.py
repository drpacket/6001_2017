# Problem 9
# 15.0 points possible (graded)
# Write a function to flatten a list. The list contains other lists, strings, or ints.
# For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is 
# flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).
# 
# def flatten(aList):
#     ''' 
#     aList: a list 
#     Returns a copy of aList, which is a flattened version of aList 
#     '''
#   
# 
# Click to expand Hint: How to think about this problem
# 
# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements. Note that we ask you to write a function only -- you cannot rely on any variables defined outside your function for your code to work correctly.
# 
# Code Editor
# 
# 1
# Paste your function here

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flat = []
    for item in aList:
        if type(item) is list:
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat






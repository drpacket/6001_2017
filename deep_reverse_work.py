# Problem 6
# 15.0 points possible (graded)
# Implement a function that meets the specifications below.
# 
# def deep_reverse(L):
#     """ assumes L is a list of lists whose elements are ints
#     Mutates L such that it reverses its elements and also 
#     reverses the order of the int elements in every element of L. 
#     It does not return anything.
#     """
#     # Your code here
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
# 
# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
# 
# Code Editor
# 
# 1
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for item in L:
        item.reverse()

L = [[1, 2], [3, 4], [5, 6, 7]]
print("---------------------------------------------------")
print(L,"(before)")
print("---------------------------------------------------")
deep_reverse(L)
print(L,"(after)")
L=[[12,15,23], [7,3,31], [9,4,21]]
print("---------------------------------------------------")
print(L,"(before)")
print("---------------------------------------------------")
deep_reverse(L)
print(L,"(after)")
print("---------------------------------------------------")




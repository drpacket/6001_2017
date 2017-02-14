#   Problem 5
#   10.0 points possible (graded)
#   Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your # #   function should return: 32
#   
#   Hint: You will need to traverse both lists in parallel.
#   
#   This function takes in two lists of numbers and returns a number.
#   
#   def dotProduct(listA, listB):
#       '''
#       listA: a list of numbers
#       listB: a list of numbers of the same length as listA
#       '''
    # Your code here

#   ---- Get pairwise products + append to list products -----
#   products = []
#   for i in lista:
#       for j in listb:
#           pair = i * j
#           result-list.append(pair)
#   ---- Add together pairwise products ----
#   result = 0 (0.0?)
#   for product in products:
#       result += product
#   ----- Return total ---------------------
#   return result
#   -------- DONE --------------------------

#   -------- WORK CODE: (!!!) --------------------

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # get pairwise-products; save in list 'products'
    products = []
    for i in range(len(listA)):
        product = listA[i] * listB[i]
        products.append(product)
    # sum pairwise-products
    result = 0
    for product in products:
        result += product
        print(result)
    # return final result (=sum of all products)
    print(result)
    return result

listA = [1, 2, 3]
listB = [4, 5, 6]

print(dotProduct(listA, listB))



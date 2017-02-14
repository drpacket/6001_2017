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
    # return final result (=sum of all products)
    return result


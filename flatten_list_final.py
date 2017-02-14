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

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print("---------------------------------------------------")
flattened = flatten(aList)
print(flattened)
print("---------------------------------------------------")

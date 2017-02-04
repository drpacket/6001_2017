def purify(input):
    output = []
    for i in input:
        if i % 2 == 0:
            output.append(i)
    return output

print(purify([1, 2, 3, 4, 5, 6]))



def product(input):
    result = 1
    for i in input:
        result *= i
    return result

print(product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))   

def search(L, e):
    for i in range(len(L)):
        print("L[i], i = ", L[i], i)
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        print("L[size-i-1] = ", L[size-i-1])
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

# test-case 1
L = []
e = 10

print("search(L, e) = ", search(L, e))
print("---------------------------------------")
print("newsearch(L, e) = ", newsearch(L, e))

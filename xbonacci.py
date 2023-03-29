def Xbonacci(signature,n):
    arr = signature
    while len(arr) < n:
        arr.append(sum(arr[-len(signature):]))
    return arr

print(Xbonacci([0,1],10))
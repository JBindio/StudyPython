def adds(*args): #parameter, arguments
    res = 0
    for i in args:
        res += i
    return res

print(adds(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(adds(1, 2, 3,))
print(adds(1, 2, 3, 4, 5))
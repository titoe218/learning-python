def odd_selection(arr: list):
    res = []
    for k in arr:
        if k % 2 == 1:
            res.append(k)
    return res

n = int(input("n = "))
arr = []
for i in range(n):
    a = input('  a[' + str(i) + '] = ')
    arr.append(int(a))
print(odd_selection(arr))

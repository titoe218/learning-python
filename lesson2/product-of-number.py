def product_number(arr: list):
    res = []
    for i in range(0, n-1):
        temp = arr[i]*arr[i+1]
        if temp % 2 == 1:
            res.append(temp)
    # sort the result array by selection sort
    for i in range(len(res)):
        min_index = i
        for j in range(i+1, len(res)):
            if res[min_index] > res[j]:
                min_index = j
        res[i], res[min_index] = res[min_index], res[i]
    return res


n = int(input("n = "))
arr = []
for i in range(n):
    a = input('  a[' + str(i) + '] = ')
    arr.append(int(a))
print(product_number(arr))

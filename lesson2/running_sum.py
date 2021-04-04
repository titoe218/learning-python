def running_sum(arr: list):
    res = []
    res.append(arr[0])
    for i in range( 1, n):
        sum=0
        for j in range(0, i+1):
            sum += arr[j]
        res.append(sum)
    return res

n = int(input("n = "))
arr = []
for i in range(n):
    a = input('  a[' + str(i) + '] = ')
    arr.append(int(a))
print(running_sum(arr))

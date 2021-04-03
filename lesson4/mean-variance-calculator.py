n = int(input("n = "))
arr = []
for i in range(n):
    a = input('  a[' + str(i) + '] = ')
    arr.append(float(a))

def sum(arr: list):
    sum = 0.0
    for i in arr:
        sum = sum + i
    return sum

def meanCalculator(arr: list):
    return sum(arr)/len(arr)

def varianceCalculator(arr: list):
    mean = meanCalculator(arr)
    s_var = 0.0
    for i in arr:
        s_var = s_var + (i - mean)**2

    return s_var/len(arr)

print("Mean: ",meanCalculator(arr))
print("Variance: %.2f" % varianceCalculator(arr))
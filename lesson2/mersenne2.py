p = int(input())
arr=[]
arr.append(4)
for i in range(1, p-1):
    temp = (pow(arr[i-1],2)-2) % (pow(2, p) - 1)
    arr.append(temp)
print(arr)
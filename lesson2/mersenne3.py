p = int(input())
arr=[]
arr.append(4)
for i in range(1, p-1):
    temp = (pow(arr[i-1],2)-2) % (pow(2, p) - 1)
    if temp == 0 and i == p-2:
        print(True)
        break
    arr.append(temp)
# print(arr)
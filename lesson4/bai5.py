import numpy as np
n = int(input("Nhap so n="))
# nhap ma tran
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
print(np.matrix(a))

laMaPhuong = False
# Kiem tra tong phan tu tren duong cheo
sum = 0
for r in range(0, n):
    for c in range(0, n):
        if(r == c):
            sum += a[r][c]

# Kiem tra tong phan tu tren cac hang
for r in range(0, n):
    sumRow = 0
    for c in range(0, n):
        sumRow += a[r][c]
    if(sum == sumRow):
        laMaPhuong = True
    else:
        laMaPhuong = False
        break

# Kiem tra tong phan tu tren cot
for c in range(0, n):
    sumCol = 0
    for r in range(0, n):
        sumCol += a[r][c]
    if(sum == sumCol):
        laMaPhuong = True
    else:
        laMaPhuong = False
        break

if(laMaPhuong == True):
    print("Ma tran A duoc goi la ma phuong")
else:
    print("Ma tran A khong la ma phuong")

n = int(input())
if n > 0 and n <= 10:
    arr = []
    max = 0
    i = 0
    while i < n:
        tmp = int(input())
        if tmp % 3 == 0 and ((tmp > 0 and max < tmp) or (tmp < 0 and max == 0)):
            max = tmp
        i += 1
    if max != 0:
        print(max)
    else:
        print("Không có số chia hết cho 3")
else:
    print("Không hợp lệ")

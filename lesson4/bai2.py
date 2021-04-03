def chinhHop(i, m):
    if(i == 0):
        return 1
    elif(i == m):
        return 1
    elif(i == 1):
        return m
    else:
        return (chinhHop(i-1, m-1) + chinhHop(i, m-1))


m = int(input())
print("Tam giac Pascal:")
for i in range(0, m+1):
    for j in range(0, i+1):
        print(chinhHop(j, i), " ")
    print()

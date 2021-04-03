# ucln 2 so n,m
def ucln(n, m):
    a = n
    b = m
    while(a != b):
        if(a > b):
            a -= b
        else:
            b -= a
    return a
# bcnn 2 so n,m


def bcnn(n, m):
    return int((n*m)/ucln(n, m))


print("Nhap phan so:")
n = int(input("Nhap tu so"))
m = int(input("Nhap tu so"))
print("Uoc so chung lon nhat: ", ucln(n, m))
print("Boi so chung nho nhat: ", bcnn(n, m))
print("Dang toi gian cua phan so:", int(n/ucln(n, m)), "/", int(m/ucln(n, m)))

def docSo(n):
    if (n == 1):
        return "một"
    elif (n == 2):
        return "hai"
    elif (n == 3):
        return "ba"
    elif (n == 4):
        return "bốn"
    elif (n == 5):
        return "năm"
    elif (n == 6):
        return "sáu"
    elif (n == 7):
        return "bảy"
    elif (n == 8):
        return "tám"
    elif (n == 9):
        return "chín"

resultStr = ""
a = int(input())
if (a>999 or a<100 or int(a/100)==0):
    print("số đã nhập không phải là số có ba chữ số")
else:
    # print("Đọc số %d bằng chữ:" % a)
    x=int(a/100)
    resultStr=str(docSo(x)) + " trăm "
    y=int((a-x*100)/10)
    z=int(a-x*100-y*10)
    if(y == 0 and z == 0):
        pass
    elif (y == 0):
        resultStr += " linh "
        resultStr += str(docSo(z))
    elif (y == 1 and z == 0):
        resultStr += " mười "
    elif (y == 1):
        resultStr += " mười "
        resultStr += str(docSo(z))
    elif (z == 0):
        resultStr += str(docSo(y)) + " mươi "
    elif (z == 1):
        resultStr += str(docSo(y)) + " mươi mốt"
    else:
        resultStr += str(docSo(y)) + " mươi "
        resultStr += str(docSo(z))
    print(resultStr)
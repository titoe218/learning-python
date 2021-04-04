import collections
n = int(input("n = "))
arr = []
for i in range(n):
    a = input('  a[' + str(i) + '] = ')
    arr.append(a)

def findMaxLettersCount(arr: list):
    result = []
    for s in arr:
        d = collections.defaultdict(int)
        for c in s:
            d[c]+=1
        result.append(sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0])
    return result

print(findMaxLettersCount(arr))
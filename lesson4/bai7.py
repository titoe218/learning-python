import random
import collections
n = int(input("n = "))
arr = []
for i in range(n):
    a = random.randint(0,n+1)
    arr.append(a)
print(arr)
highest = max(arr)
lowest = min(arr)
d = collections.defaultdict(int)
for c in arr:
    d[c]+=1
print("Highest: ", highest)
print("Lowest: ", lowest)
print("Freq: ", sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0])
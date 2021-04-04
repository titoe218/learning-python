import collections
d = collections.defaultdict(int)
s = input("")
for c in s:
    d[c]+=1
print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0])
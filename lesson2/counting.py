arr = input()
count = 0
for c in arr:
    if ord(c) != 32:
        count +=1

print(count)
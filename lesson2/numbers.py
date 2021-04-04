start = int(input())
end = int(input())

odd_arr = []
even_arr = []
for i in range(start, end+1):
    if i % 2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)
print(odd_arr)
print(even_arr)
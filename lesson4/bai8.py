str = input("").split(" ")
 
count={}
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
 
res = sorted(count, key=count.get, reverse=True)
print(res[0])
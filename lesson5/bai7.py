import os
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
content.reverse()

with open('reverse.txt', 'w') as f:
    for item in content:
        f.write("%s\n" % item)
# while True:
#     i = input("")
#     if not i:
#         break
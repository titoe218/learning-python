import os

s = input().split()
if s[0] == "mkdir":
    os.mkdir(s[1])
elif s[0] == "mkfile":
    os.mkfile(s[1])
elif s[0] == "ls":
    os.ls(s[1])
elif s[0] == "cd":
    os.cd(s[1])
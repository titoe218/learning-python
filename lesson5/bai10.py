import sys
import tty
import termios


class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
current_index = 0

# for i in range(0, 20):
inkey = _Getch()
while(True):
    while(True):
        k = inkey()
        if k != '':
            break
    if k == '\x1b[A':
        if current_index == 0:
            current_index = len(content) - 1
        else:
            current_index = current_index - 1
        print(content[current_index])
    elif k == '\x1b[B':
        if current_index == len(content) - 1:
            current_index = 0
        else:
            current_index = current_index + 1
        print(content[current_index])
    else:
        print("not an arrow key!")
        break
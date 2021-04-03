from pynput.keyboard import Listener, Key


def read_file(file_name):
    list_str = []
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            list_str.append(line)
    return(list_str)


pos = 0
list_line = read_file('input.txt')
print(list_line)


def on_press(key):
    global pos
    if key == Key.up:
        pos -= 1
        if pos < 0:
            pos = 0
        else:
            print(list_line[pos])
    if key == Key.down:
        pos += 1
        if pos > len(list_line) - 1:
            pos = len(list_line) - 1
        else:
            print(list_line[pos])
    if key == Key.esc:
        # Stop listener
        return False


with Listener(on_press=on_press) as listener:
    listener.join()
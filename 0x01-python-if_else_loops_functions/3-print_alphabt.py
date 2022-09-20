#!/usr/bin/python3
i = 96
while i < 123:
    i += 1
    if i == 101 or i == 113:
        continue
    print("{}".format(chr(i)), end="")

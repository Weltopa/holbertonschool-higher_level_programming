#!/usr/bin/python3
for i in range(0, 10):
    x = i + 1
    for x in range(x, 10):
        print("{}{}".fomrat(i, x), end="")
        if i == 8 and x == 9:
            print()
        else:
            print(", ", end="")

#!/usr/bin/python3
for i in range(89):
    if i / 10 < i % 10:
        print("{:0>2d},".format(i), end=" ")
print("{:0>2d}".format(i + 1))

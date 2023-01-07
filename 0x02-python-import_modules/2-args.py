#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv[1:]
    num_arg = len(argv)
    line1 = "{:d} argument".format(num_arg)
    if num_arg == 0:
        line1 += "s."
    elif num_arg == 1:
        line1 += ":"
    else:
        line1 += "s:"
    print(line1)
    for i, arg in enumerate(argv):
        print("{:d}: {:s}".format(i + 1, arg))

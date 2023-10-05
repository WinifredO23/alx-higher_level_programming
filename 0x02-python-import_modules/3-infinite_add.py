#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum_argv = 0

    for i in range(len(sys.argv) - 1):
        sum_argv += int(sys.argv[i + 1])
    print("{}".format(sum_argv))

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    i = 1
    if argv_count is 0:
        print("{:d} arguments.".format(argv_count))
    elif:
        print("{:d} argument:".format(argv_count))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_count))
        while i <= argv_count:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1



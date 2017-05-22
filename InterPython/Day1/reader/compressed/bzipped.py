import sys
import bz2

opener = bz2.open


def main():
    f = bz2.open(sys.argv[1], mode='wt')
    f.write(" ".join(sys.argv[2:]))
    f.close()


if __name__ == '__main__':
    main()
    exit(0)
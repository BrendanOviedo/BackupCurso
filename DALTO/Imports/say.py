import cowsay
import sys


if len(sys.argv) == 2:
    cowsay.cow(sys.argv[1])
import sys

for line in sys.stdin:
    nums = line.strip().split()
    print(" ".join([str(i) for i in sorted([int(i) for i in nums])]))
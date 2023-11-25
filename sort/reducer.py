import sys
all_nums = []
for line in sys.stdin:
    kvs = line.strip().split()
    kvs = [int(i) for i in kvs]
    if not all_nums:
        all_nums.append(kvs)
    else:
        l1 = all_nums.pop()
        l2 = kvs
        new_nums = []
        index1 = 0
        index2 = 0
        while index1 < len(l1) and index2 < len(l2):
            a = l1[index1]
            b = l2[index2]
            if a < b:
                new_nums.append(a)
                index1 += 1
            else:
                new_nums.append(b)
                index2 += 1

        if index1 == len(l1) and index2 < len(l2):
            new_nums.extend(l2[index2: ])
        if index1 < len(l1) and index2 == len(l2):
            new_nums.extend(l1[index1: ])

        all_nums.append(new_nums)
print(all_nums[0])
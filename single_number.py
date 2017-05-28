import collections


def single_number(nums):
    d = collections.defaultdict(int)
    for i in nums:
        d[i] += 1
    for k, v in d.items():
        if v == 1:
            return k


def single_number1(nums):
    return (sum(set(nums)) * 3 - sum(nums)) / 2


print single_number([3, 3, 3, 2])
print single_number1([3, 3, 3, 2])

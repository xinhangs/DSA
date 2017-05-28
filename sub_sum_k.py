import collections


def sub_sum_k(nums, k):
    counts = collections.Counter()
    counts[0] = 1
    ret = s = 0
    for x in nums:
        s += x
        ret += counts[s - k]
        counts[s] += 1
    return ret


nums = [-1, 2, -3, 4, -1, 0]
k = 1
print sub_sum_k(nums, k)

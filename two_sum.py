def two_sum(nums, target):
    d = {v: i for i, v in enumerate(nums)}
    same = 0
    for k in d:
        c = target - k
        if c in d:
            if c != k:
                return [d[k], d[c]]
            else:
                same = k
    ret = [i for i, v in enumerate(nums) if v == same]
    if len(ret) == 2:
        return ret


def two_sum1(nums, target):
    d = {}
    same = 0
    for i, v in enumerate(nums):
        d[v] = i
        c = target - v
        if c in d:
            if c != v:
                return [d[v], d[c]]
            else:
                same = v
    ret = [i for i, v in enumerate(nums) if v == same]
    if len(ret) == 2:
        return ret


print two_sum1([3, 3], 6)
print two_sum1([2, 7, 11, 15], 9)

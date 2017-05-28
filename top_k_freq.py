import operator


def top_k_freq(nums, k):
    d = {}
    for i in nums:
        d[i] = d[i] + 1 if i in d else 1
    sort_lst = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    return [x[0] for x in sort_lst][:k]


print top_k_freq([-1, -1], 1)
print top_k_freq([4, 4, 4, 5, 5, 6], 2)

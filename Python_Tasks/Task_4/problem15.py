# 15
# Word Order
# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict
od = OrderedDict()
for _ in range(int(input())):
    k = input()
    od[k] = od.get(k, 0) + 1
print(len(od))
print(*od.values())
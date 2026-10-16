# 13
# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

size1 = int(input())
set1 = input()
size2 = int(input())
set2 = input()

setone = set(map(int, set1.split()))
settwo = set(map(int, set2.split()))

final_set = (setone.difference(settwo)).union(settwo.difference(setone))

for i in sorted(final_set):
    print(i)
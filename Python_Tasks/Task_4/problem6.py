# 6
# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


n = int(input())
arr = list(map(int, input().strip()))

score = sorted(set(arr))
print(score[-2])

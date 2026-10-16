# 12
# Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    sums = sum(set(array))
    avg = sums / len(set(array))
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
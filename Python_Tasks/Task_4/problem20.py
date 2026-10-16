# 20
# No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

import sys

def happiness_calculator(input_data):
    n, m = map(int, input_data[0].split())

    array = list(map(int, input_data[1].split()))
    a = set(map(int, input_data[2].split()))
    b = set(map(int, input_data[3].split()))

    happiness = 0

    for x in array:
        if x in a:
            happiness += 1
        elif x in b:
            happiness -= 1

    print(happiness)


if __name__ == '__main__':
    input_data = sys.stdin.read().splitlines()
    happiness_calculator(input_data)
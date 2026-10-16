# 11
# String Validators
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    j = 0
    isalnum, isalpha, isdigit, islower, isupper = False, False, False, False, False
    isall = False
    
    while j < len(s) and isall == False:
        if s[j].isalnum():
            isalnum = True
        if s[j].isalpha():
            isalpha = True
        if s[j].isdigit():
            isdigit = True
        if s[j].islower():
            islower = True
        if s[j].isupper():
            isupper = True
        if isalnum and isalpha and isdigit and islower and isupper:
            isall = True
        j += 1
        
    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)
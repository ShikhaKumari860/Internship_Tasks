# 16
# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    st = [] 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        st.append([name,score])
        
    min_val = sorted({ s for _,s in st})[1]
    print(*sorted([name for name,v in st if v == min_val]),sep='\n') 
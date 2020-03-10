def solution(A):
    B = set(sorted(A))
    print(B)
    m = 1
    for x in B:
        if x == m:
            m+=1
    return m

x = [1, 3, 6, 4, 1, 2]
print(solution(x))
def is_zero(n : int, ind : int) -> int:
    if ((n & (1 << ind)) == 0):
        return 0
    else:
        return 1

def count( n:int, ind:int) -> int:
    res = 0
    while is_zero(n, ind) != 1:
        ind+=1
        if (ind == 32):
            return 0
        res+=1
    return res

def solution(num:int) -> int:
    result = 0
    for i in range(32):
        if is_zero(num, i):
            t = count(num, i + 1)       
            if result < t:
                result = t
            else:
                result = result
    return result

# Given Test Case
print(solution(5))

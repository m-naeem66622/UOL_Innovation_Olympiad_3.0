def solution(arr):
    if max(arr) <= 0:
        return 1

    num = max(arr) + 1
    s = [0] * max(arr)

    for i in arr:
        if i > 0:
            s[i - 1] = 1

    for i in range(len(s)):
        if s[i] == 0:
            num = i + 1
            break

    return num

# Given Test Case
arr = [1, 3, 6, 4, 1, 2]
print(solution(arr))

arr = [1, 2, 3]
print(solution(arr))

arr = [-1, -3]
print(solution(arr))
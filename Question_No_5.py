def solution(arr_a, arr_b):
    arr = [0] * (len(arr_a) + 1)
    arr[0] = 1
    arr[1] = 1
    max = 1 << 30

    for i in range(2, len(arr)):
        arr[i] = (arr[i-1] + arr[i-2]) % max

    final_arr = [0] * len(arr_a)

    for i in range(len(arr_a)):
        final_arr[i] = arr[arr_a[i]] % (1 << arr_b[i])

    return final_arr

# Given Test Case
arr_1 = [4, 4, 5, 5, 1]
arr_2 = [3, 2, 4, 3, 1]
print(solution(arr_1, arr_2))
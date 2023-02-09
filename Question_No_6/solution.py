def gt_com_div(a, b):
    if a % b == 0:
        return b
    else:
        return gt_com_div(b, a % b)


def solution(arr_a, arr_b):
    final_result = 0

    for i in range(len(arr_a)):
        a = arr_a[i]
        b = arr_b[i]
        d = gt_com_div(a, b)
        c = 0

        while c != 1:
            c = gt_com_div(a, d)
            a = a / c
        c = 0

        while c != 1:
            c = gt_com_div(b, d)
            b = b / c

        if a == 1 and b == 1:
            final_result += 1

    return final_result


# Given Test Case
arr1 = [15, 10, 3]
arr2 = [75, 30, 5]
print(solution(arr1, arr2))

def max_cross(arr, low, mid, high, limit):
    left_best = float('-inf')
    left_sum = 0
    left_part = None

    s = 0
    for i in range(mid, low - 1, -1):
        s += arr[i]
        if s <= limit and s > left_best:
            left_best = s
            left_part = arr[i:mid+1]

    right_best = float('-inf')
    right_sum = 0
    right_part = None

    s = 0
    for j in range(mid+1, high+1):
        s += arr[j]
        if s <= limit and s > right_best:
            right_best = s
            right_part = arr[mid+1:j+1]

    if left_best == float('-inf') and right_best == float('-inf'):
        return float('-inf'), None
    if left_best == float('-inf'):
        return right_best, right_part
    if right_best == float('-inf'):
        return left_best, left_part

    total = left_best + right_best
    if total <= limit:
        return total, left_part + right_part
    else:
        if left_best >= right_best:
            return left_best, left_part
        else:
            return right_best, right_part


def solve(arr, low, high, limit):
    if low == high:
        if arr[low] <= limit:
            return arr[low], [arr[low]]
        else:
            return float('-inf'), None

    mid = (low + high) // 2

    left_val, left_arr = solve(arr, low, mid, limit)
    right_val, right_arr = solve(arr, mid+1, high, limit)
    cross_val, cross_arr = max_cross(arr, low, mid, high, limit)

    best = max(left_val, right_val, cross_val)

    if best == left_val:
        return left_val, left_arr
    elif best == right_val:
        return right_val, right_arr
    else:
        return cross_val, cross_arr


def find_best(arr, limit):
    if not arr or limit <= 0:
        return None, 0
    ans, sub = solve(arr, 0, len(arr)-1, limit)
    if ans == float('-inf'):
        return None, 0
    return sub, ans


# testing
tests = [
    ([2,1,3,4], 5),
    ([2,2,2,2], 4),
    ([1,5,2,3], 5),
    ([6,7,8], 5),
    ([1,2,3,2,1], 5),
    ([1,1,1,1,1], 4),
    ([4,2,3,1], 5),
    ([], 10),
    ([1,2,3], 0),
    (list(range(1,100001)), 10**9)
]

for i, (arr, c) in enumerate(tests, 1):
    sub, s = find_best(arr, c)
    print("Test-", i, ": Best =", sub, "Sum =", s)

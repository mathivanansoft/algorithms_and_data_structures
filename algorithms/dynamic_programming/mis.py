# maximum_sum_increasing_subsequence

def mis(arr, curr, pre, max_sum):
    # using recursion
    if len(arr) == 1:
        return arr[0]
    elif curr >= len(arr):
        return max_sum
    elif pre == -1:
        return max (
            mis(arr, curr+1, curr, max_sum+arr[curr]),
            mis(arr, curr+1, pre, max_sum)
            )
    elif pre != -1:
        if arr[curr] > arr[pre]:
            return max(
                mis(arr, curr+1, curr, max_sum+arr[curr]),
                mis(arr, curr+1, pre, max_sum)
            )
        else:
            return mis(arr, curr+1, pre, max_sum)

def maximum_sum_increasing_subsequence(arr):
    max_sum = arr[:]

    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[i] > arr[j] and max_sum[j] + arr[i] > max_sum[i]:
                max_sum[i] = max_sum[j] + arr[i]

    return max(max_sum)
            

if __name__ == "__main__":
    # arr = [50, 9, 2, 7, 3, 1, 8, 4, 5, 6]
    arr = [20, 3, 1, 15, 16, 2, 12, 13]
    # print(mis(arr, 0, -1, 0))
    print(maximum_sum_increasing_subsequence(arr))

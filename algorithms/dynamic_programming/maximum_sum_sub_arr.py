
def naive_approach(arr):
    # Generate all possible sub arrays
    # find the max sum in sub arrays

    start, end = 0, 1
    max_sum = 0

    for index in range(0, len(arr)):
        for inner_index in range(0, len(arr)):
            cur = inner_index
            temp_sum = 0
            if len(arr) - inner_index >= index+1:
                for _ in range(0, index+1):
                    temp_sum += arr[cur]
                    cur += 1
                if temp_sum > max_sum:
                    start = inner_index
                    end = cur
                    max_sum = temp_sum

    print ("start ", start, "end ", end, "sum", max_sum)

def approach2(arr):
    # store the cumulative sum
    temp = []
    for elmnt in arr:
        if len(temp) == 0:
            temp.append(elmnt)
        else:
            temp.append(temp[-1]+elmnt)

    max_sum = 0
    start, end = 0, 1
    print ("cumulative sum", temp)
    for index in range(len(arr)-1, -1, -1):
        for inner_index in range(index-1, -2, -1):
            if inner_index == -1: 
                temp_sum = temp[index]-0
            else:
               temp_sum = temp[index]-temp[inner_index] 

            if  temp_sum > max_sum:
                max_sum = temp_sum
                end = index + 1
                start = inner_index +1
    # end excluded
    print ("start ", start, "end ", end, "sum", max_sum)
            
def kadane_algorithm(arr):
    # atleast one element should be positive
    max_sum = 0
    cur_sum = 0
    end = -1

    for index, elmnt in enumerate(arr):
        cur_sum += elmnt
        if cur_sum < 0:
            cur_sum = 0
        if max_sum < cur_sum:
            max_sum = cur_sum
            end = index

    # end inclusive
    print("Max sum", max_sum, "end", end)


if __name__ == "__main__":
    arr = [10, -5, -3, 4, 2, 12, -8, -12, 19]
    #naive_approach(arr)
    #approach2(arr)
    kadane_algorithm(arr)

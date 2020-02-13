# Find the longest subsequence in array in which the elements in subsequence
# are consecutive


def longest_subsequence(arr):
    dt = {}
    for elmnt in arr:
        dt.update({elmnt: False})

    start = -1
    end = -1
    maximum = 0
    data = 0
    for index, elmnt in enumerate(arr):
        if dt.get(elmnt) is False:
            temp = elmnt
            while True:
                if temp in dt:
                    temp -=1
                else:
                    temp +=1
                    start = temp
                    break
            while True:
                if temp in dt:
                    dt.update({temp: True})
                    temp += 1
                else:
                    end = temp
                    if end-start > maximum:
                        maximum = end - start
                        data = end-1
                    break
    print("Maximum consecutive", maximum)
    for index in range(data-maximum+1, data+1):
        print(index, end= " ")

if __name__ == "__main__":
    arr = [10, 4, 3, 11, 13, 5, 6, 12, 7]
    longest_subsequence(arr)
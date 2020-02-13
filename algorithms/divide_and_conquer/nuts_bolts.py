# nuts and bolts
# should not compare two nuts and two bolts
# find the pair of nuts and bolts of equal size

def match_nuts_and_bolts(nuts, bolts, start, end):
    if start < end:
        pindex = partition(bolts, start, end, nuts[end])
        partition(nuts, start, end, bolts[pindex])
        match_nuts_and_bolts(nuts, bolts, start, pindex-1)
        match_nuts_and_bolts(nuts, bolts, pindex+1, end)

def partition(arr1, start, end, pivot):
    temp = start
    for index in range(start, end):
        if arr1[index] == pivot:
            t = arr1[index]
            arr1[index] = arr1[end]
            arr1[end] = t
            
        if arr1[index] < pivot:
            t = arr1[index]
            arr1[index] = arr1[temp]
            arr1[temp] = t
            temp += 1
    
    t = arr1[temp]
    arr1[temp] = arr1[end]
    arr1[end] = t
    return temp


if __name__ == "__main__":
    nuts = [1, 3, 4, 2, 6, 5]
    bolts = [5, 6, 2, 4, 3, 1]
    print(match_nuts_and_bolts(nuts, bolts, 0, len(nuts)-1))
    print("Nuts", nuts)
    print("Bolts", bolts)
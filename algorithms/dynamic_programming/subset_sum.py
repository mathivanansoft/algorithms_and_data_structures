# subset sum
# it works only for positive integers

def subset_sum(subset, total):
    output = [[False for j in range(0, total+1)] for i in range(0, len(subset)+1)]
    for i in range(0, len(subset)+1):
        output[i][0] = True
    for i in range(1, len(subset)+1):
        for j in range(1, total+1):
            if subset[i-1] <= j:
                val = subset[i-1]
                output[i][j] = output[i-1][j-val] or output[i-1][j]
            else:
                output[i][j] = output[i-1][j]
    return output[-1][-1]

if __name__ == "__main__":
    total = 5
    subset = [6,3,2,1,4]
    print(subset_sum(subset, total))
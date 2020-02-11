# 0/1 knapsack

def knapsack(items, capacity):
    output = [[0 for j in range(0, capacity+1)] for i in range(0, len(items)+1)]
    for i in range(1, len(items)+1):
        for j in range(1, capacity+1):
            if items[i-1]["weight"] <= j:
                wt = items[i-1]["weight"]
                output[i][j] = max(items[i-1]["profit"]
                                   + output[i-1][j-wt],
                                   output[i-1][j])
            else:
                output[i][j] = output[i-1][j]
    return output[-1][-1]

if __name__ == "__main__":
    items = [
        {
            "name": "A",
            "profit": 10,
            "weight": 1
        },
        {
            "name": "B",
            "profit": 12,
            "weight": 2
        },
        {
            "name": "C",
            "profit": 28,
            "weight": 4
        }
    ]
    capacity = 6
    print("Maximum Profit", knapsack(items, capacity))
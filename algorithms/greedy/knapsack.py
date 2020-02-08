# knapsack based on profit/weight

def knapsack(items, tot_weight):
    for item in items:
        profit = item.get("profit")
        weight = item.get("weight")
        pw = profit / weight
        item.update({"pro_by_weight": pw})
    items = sorted(items, key=lambda item: item["pro_by_weight"], reverse=True)
    total_profit = 0
    for item in items:
        wt = item.get("weight")
        if wt <= tot_weight:
            tot_weight -= wt
            pf = item.get("profit")
            total_profit += pf
        else:
            break
    if tot_weight > 0:
        ratio = item.get("pro_by_weight")
        total_profit += (ratio * tot_weight)
    return total_profit

if __name__ == "__main__":
    items = [
        {
            "name": "Obj1",
            "profit": 25,
            "weight": 18
        },
        {
            "name": "Obj2",
            "profit": 24,
            "weight": 15
        },
        {
            "name": "Obj3",
            "profit": 15,
            "weight": 10
        }
    ]
    tot_weight = 20
    print("MAXIMUM PROFIT", knapsack(items, tot_weight))
    
    items = [
        {
            "name": "Obj1",
            "profit": 10,
            "weight": 2
        },
        {
            "name": "Obj2",
            "profit": 5,
            "weight": 3
        },
        {
            "name": "Obj3",
            "profit": 15,
            "weight": 5
        },
        {
            "name": "Obj4",
            "profit": 7,
            "weight": 7
        },
        {
            "name": "Obj5",
            "profit": 6,
            "weight": 1
        },
        {
            "name": "Obj6",
            "profit": 18,
            "weight": 4
        },
        {
            "name": "Obj7",
            "profit": 3,
            "weight": 1
        }
    ]
    tot_weight = 15
    print("MAXIMUM PROFIT", knapsack(items, tot_weight))
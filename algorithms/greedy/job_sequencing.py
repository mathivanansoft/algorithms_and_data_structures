# find the maxmimum profit by scheduling jobs

def find_maximum_profit(jobs):
    endtime = 0
    for job in jobs:
        dl = job["deadline"]
        endtime = max(endtime, dl)
    output = [0 for i in range(0, endtime)]
    for job in jobs:
        deadline = job["deadline"]
        for index in range(deadline - 1, -1, -1):
            if output[index] == 0:
                output[index] = job["profit"]
                break
    print(output)
    return sum(output)
            
    
    
if __name__ == "__main__":
    jobs = [
        {
            "name": "J1",
            "deadline": 2,
            "profit": 6
        },
        {
            "name": "J2",
            "deadline": 1,
            "profit": 8
        },
        {
            "name": "J3",
            "deadline": 1,
            "profit": 5
        },
        {
            "name": "J4",
            "deadline": 2,
            "profit": 10
        }
    ]
    jobs = sorted(jobs, key=lambda job: (-job["profit"]))
    print("Jobs", jobs)
    print("Profit", find_maximum_profit(jobs))
    jobs = [
        {
            "name": "J1",
            "deadline": 5,
            "profit": 200
        },
        {
            "name": "J2",
            "deadline": 3,
            "profit": 180
        },
        {
            "name": "J3",
            "deadline": 3,
            "profit": 190
        },
        {
            "name": "J4",
            "deadline": 2,
            "profit": 300
        },
        {
            "name": "J5",
            "deadline": 4,
            "profit": 120
        },
        {
            "name": "J6",
            "deadline": 2,
            "profit": 100
        }
    ]
    jobs = sorted(jobs, key=lambda job: (-job["profit"]))
    print(jobs)
    print("Profit", find_maximum_profit(jobs))
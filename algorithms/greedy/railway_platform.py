# Find the minimum number of platform required in a railway station without
# collision with each other

def find_min_platforms(trains):
    timings = []
    for train in trains:
        timings.append(
            (train["arrival"], "A")
        )
        timings.append(
            (train["departure"], "D")
        )
    timings = sorted(timings, key=lambda timing: (timing[0]))
    count = 0
    minimum = 0
    for timing in timings:
        if timing[1] == "A":
            count += 1
        else:
            minimum = max(count, minimum)
            count -= 1
    return minimum 

if __name__ == "__main__":
    trains = [
        {
            "name": "A",
            "arrival": 10.00,
            "departure": 10.20
        },
        {
            "name": "B",
            "arrival": 10.15,
            "departure": 14.00
        },
        {
            "name": "C",
            "arrival": 10.30,
            "departure": 15.00
        },
        {
            "name": "D",
            "arrival": 10.40,
            "departure": 10.55
        }
    ]
    print("MIN REQUIRED PLATFORMS", find_min_platforms(trains))
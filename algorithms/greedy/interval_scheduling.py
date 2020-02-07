# pick the maximum number of intervals in such a way that intervals
# should not overlap each other

def max_intervals(intervals):
    output = []
    for interval in intervals:
        if not output:
            output.append(interval)
        else:
            if output[-1][1] < interval[0]:
                output.append(interval)
    return output


if __name__ == "__main__":
    intervals = [(10, 13), (9, 14), (7, 11), (12, 16), (20, 25), (1, 50)]
    intervals = sorted(intervals, key=lambda interval: (interval[1]))
    output = max_intervals(intervals)
    print("INTERVALS:: ", output)
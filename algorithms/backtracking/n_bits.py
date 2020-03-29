

def generate_bits(arr, start, end):
    # start is inclusive
    # end is exclusive

    if start == end:
        print("".join(map(str, arr)))
    else:
        arr[start] = 0
        generate_bits(arr, start+1, end)
        arr[start] = 1
        generate_bits(arr, start+1, end)
                


if __name__ == "__main__":
    arr = [0, 0, 0]
    bits = [0, 1]
    generate_bits(arr, 0, len(arr))
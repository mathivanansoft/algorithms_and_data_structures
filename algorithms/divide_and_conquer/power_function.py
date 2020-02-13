   
def power(base, n):
    if n == 0:
        return 1
    val = power(base, n // 2)

    if n & 1:
        return val * val * base
    else:
        return val * val

if __name__ == "__main__":
    print(power(2, 5))
    print(power(2, 4))
    print(power(3, 4))
    print(power(3, 5))
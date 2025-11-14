def simple_div(num):
    count = 2
    while count**2 <= num:
        if num % count == 0:
            num //= count
        else:
            count += 1
    return num

if __name__ == "__main__":
    n = 600851475143
    print(simple_div(n))
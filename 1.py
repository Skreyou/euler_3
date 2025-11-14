def simple_div(num):
    count = 2
    while count**2 <= num:
        if num % count == 0:
            num //= count
        else:
            count += 1
    return count

if __name__ == "__main__":
    n = 13195
    print(simple_div(n))
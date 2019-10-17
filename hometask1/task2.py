def sum_num(x):
    num = x
    sum = 0
    while x != 0:
        sum += x % 10
        x //= 10
    return (sum, num)
def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort(key = sum_num)
    print(*a)
if __name__ == "__main__":
    main()

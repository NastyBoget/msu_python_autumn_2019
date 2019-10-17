n, k = (int(i) for i in input().split())
while n > k:
    print(1, end=' ')
    print(2, end=' ')
    n -= 2
if n == k:
    for i in range(1, k + 1):
        print(i, end=' ')
else:
    print(1, end=' ')
    for i in range(3, k + 1):
        print(i, end=' ')

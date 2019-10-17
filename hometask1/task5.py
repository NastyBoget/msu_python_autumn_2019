def main():
    base = 0
    for i in range(4, -1, -1):
        res = []
        for j in range(1, 11):
            print('? {}'.format(base + j * 10**i))
        print('+')
        for j in range(10):
            res.append(int(input()))
        if res[9] == 0:
            print('! {}'.format(base + 10**(i + 1)))
            return 0
        j = 0
        while (res[j] == 0):
            j += 1
        base += j * 10**i
    return base
res = main()
if res != 0:
    print('! {}'.format(res))

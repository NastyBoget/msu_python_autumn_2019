n = int(input())
a = [int(i) for i in input().split()]
n1 = 0
a1 = []
for i in a:
    if i not in a1:
        a1.append(i)
    else:
        n1 += 1
print(*a1)
print(n1)

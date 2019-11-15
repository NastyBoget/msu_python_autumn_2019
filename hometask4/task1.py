def solution1(arg):
    return [x*4 for x in arg]
def solution2(arg):
    return [x*(arg.index(x) + 1) for x in arg]
def solution3(arg):
    return [x for x in arg if x % 3 == 0 or x % 5 == 0]
def solution4(arg):
    return [y for x in arg for y in x]
def solution5(arg):
    return [(i, j, int((i**2 + j**2)**(1/2))) for i in range(1, arg) \
 for j in range(i + 1, arg + 1) if (i**2 + j ** 2 <= arg**2) and \
 ((i**2 + j ** 2)**(1/2) - int((i**2 + j ** 2)**(1/2))== 0)]
def solution6(a):
    return [[a[1][j] + a[0][i] for j in range(len(a[1]))] for i in range(len(a[0]))]
def solution7(a):
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]
def solution8(a):
    return [list(map(int, x.split())) for x in a]
def solution9(arg):
    return {chr(ord('a') + v): v**2 for v in arg}
def solution10(a):
    return {chr(ord(x[0])+ord('A')-ord('a'))+x[1:] \
    for x in set([y.lower() for y in a if len(y) > 3])}
solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}

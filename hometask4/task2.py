from functools import reduce
from operator import add
from operator import setitem
def solution1(arg):
    return list(map(lambda x: int(reduce(add, list(filter \
(lambda y: y >= '0' and y <= '9', x)))[::-1]), arg)) 
def solution2(arg):
    return list(map(lambda x: x[0] * x[1],
         list(arg)))
def solution3(arg):
    return list(filter(lambda x: x % 6 == 0 or x % 6 == 2 or x % 6 == 5,
           arg))
def solution4(arg):
    return list(filter(lambda x: bool(x), arg))
def solution5(arg):
    return list(map(lambda x: setitem(x, 'square', 
x['width'] * x['length']), arg))
def solution6(arg):
    return list(map(lambda x: dict(x, square=x['width'] *
x['length']), arg))
def solution7(arg):
    return reduce(lambda x, y: x.intersection(y),arg)
def solution8(arg):
    return reduce(lambda d, x: setitem(d, x, d.pop(x, 0) + 1) or d,
       arg, {})
def solution9(arg):
    return list(map(lambda x: x['name'],
list(filter(lambda d: d['gpa'] > 4.5, arg))))
def solution10(arg):
    return list(filter(lambda x: sum(list(map(int,x[::2])))
== sum(list(map(int, x[1::2]))), arg))
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

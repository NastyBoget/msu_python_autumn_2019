def gen(n, left, right, res):
    if(left + right == 2 * n):
        yield res
    if(left < n):
        yield from gen(n, left + 1, right, res + '(')
    if(right < left):
        yield from gen(n, left, right + 1, res + ')')
def brackets(n):
    yield from gen(n, 0, 0, '')
try:
    n = int(input())
    print(*list(brackets(n)), sep='\n')
except:
    pass

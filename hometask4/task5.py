def product(a):
    if not a:
        yield ()
    else:
        for x in a[0]:
            for y in product(a[1:]):
                yield (x,) + y

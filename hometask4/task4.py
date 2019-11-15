def counter(func): #декоратор вызывается 1 раз когда декорируется функция
    counter.rdepth = 0
    counter.maxdepth = 0
    import functools
    @functools.wraps(func)    
    def wrapper(*args, **kwargs): #обертка вызывается каждый раз когда вызывается функция
        if counter.rdepth == 0:
            counter.maxdepth = 0
            wrapper.ncalls = 0
        wrapper.ncalls += 1
        counter.rdepth += 1
        if counter.rdepth > counter.maxdepth:
            counter.maxdepth = counter.rdepth
        wrapper.rdepth = counter.maxdepth
        res = func(*args, **kwargs)
        counter.rdepth -= 1
        return res
    wrapper.ncalls = 0
    wrapper.rdepth = 0
    return wrapper

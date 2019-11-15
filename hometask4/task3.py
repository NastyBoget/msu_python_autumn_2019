import time
def timeout(rps):
    def decorator(func):
        import functools
        @functools.wraps(func)    
        def wrapper(*args, **kwargs):
            t = time.time()
            res = func(*args, **kwargs)
            delta_t = time.time() - t
            if delta_t < 1 / float(rps):
                time.sleep(1 / float(rps) - delta_t)
            return res
        return wrapper
    return decorator

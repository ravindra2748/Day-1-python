import time
import functools

def log_time(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4}s")
        return result
    return wrapper

@log_time
def slow_process():
    time.sleep(3)

slow_process()
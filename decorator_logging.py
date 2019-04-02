from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + ' was called.'
            print(log_string)
            # open the log file and append
            with open(logfile, 'a') as f:
                # Now log to the specified log file.
                f.write(log_string + '\n')
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()

from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print('Hey let do something fun before executing the a_func().')
        a_func()
        print('Hey let go for a drink after executing the a_func().')
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print('Ahhaaa... I am so boring. I need decoration!!!!!.')

a_function_requiring_decoration()
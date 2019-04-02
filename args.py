

def test_var_args(f_arg, *argv):
    print(f'First argument: {f_arg}.')
    for arg in argv:
        print(f'Another argument through *argv: {arg}.')

test_var_args('Hello, World!!!', 'Welcome to the Python world', "Let's have some fun with coding")
#test_var_args('Hello, World!!!')
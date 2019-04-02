


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')
b = 'hi'
greet_me(name='Hello, World!!!')
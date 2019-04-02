
def generator_function():
    for i in range(10):
        yield i
        print(f'hi: {i}' )

for item in generator_function():
    print(item)
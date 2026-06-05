#arbitary arguments
def my_function(*args):
    print("The arguments are:")
    for arg in args:
        print(arg)
my_function("Hello", "World", 42, [1, 2, 3])

def my_function(**kwargs):
    print("The keyword arguments are:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function(name="Alice", age=30, city="New York")
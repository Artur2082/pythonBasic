def counter(func):
    def add_one(*args, **kwargs):
        add_one.calls += 1
        print(f"Call {add_one.calls} of {func.__name__}")
        return add_one.calls
    add_one.calls = 0
    return add_one


@counter
def example_function():
    print("Inside the function")

example_function()
example_function()
example_function()
example_function()

def add_decorator(number):
    def decorator(func):
        def wrapped(func_arg):
            return func(func_arg) + number
        return wrapped
    return decorator

@add_decorator(5)
def example_function(x):
    return x * 2

print(example_function(2))
print(example_function(0))
print(example_function(-5))
print(example_function(3))


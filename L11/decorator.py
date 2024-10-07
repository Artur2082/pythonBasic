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



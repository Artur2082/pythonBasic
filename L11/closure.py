def closure_example(x):
    def inner_function(y):
        nonlocal x
        x = x + y
        return x
    return inner_function


test1 = closure_example(5)
print('test1 = ', test1(3))
test2 = closure_example(-2)
print('test2 = ', test2(5))
test3 = closure_example(10)
print('test3 = ', test3(2))
print('test3 = ', test3(5))
test4 = closure_example(-8)
print('test4 = ', test4(10))
print('test4 = ', test4(-4))

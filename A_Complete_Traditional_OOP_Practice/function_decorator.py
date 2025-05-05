
def add_sum_num(fn):
    def inner(*args, **kwargs):
        print("Sum of numbers")
        print("Sum of numbers", args, kwargs)
        print(args[0] + args[1])
        return fn(*args, **kwargs)
    return inner

@add_sum_num
def add(a, b):
    pass

add(2,2)
#*args and **kwargs follow positional arguments and if we change the postion of parameter without changing arguments we will get error
def test(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total = total+item
    return sum(args)+total
print(test(1,2,3, a=12, b=23, c=24))

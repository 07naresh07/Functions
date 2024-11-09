#*args is used to store multiple values
#We can define other variables inplace of *args like *hello, *name etc.
#If we print args (without *) alone, it gives tuples
def checkArgs(*args):
    print(*args)
    return sum(args)
print(checkArgs(1,2,4,6))
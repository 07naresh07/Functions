def outer():
    x='local'
    def inner():
        nonlocal x
        x= 'nonlocal'
        print("Inner: ",x)
    inner()
    print("Outer: ",x)
outer()

#A nonlocal variable uses variables from parent function and next time if value is assigned, it modifies the parent variable
# If we are defining multiple parameters including *args and **kwargs order should be following:
    #1. parameters (like name, age, sex)
    #2. *args
    #3. default parameters (like name="naresh", age=29, sex="male")
    #4. **kwargs
def display(name, *args, sex="male", **kwargs):
    print(f"My name is {name}, I am {args} years old. I am {sex} by sex and my info is {kwargs}")
display("Naresh", 29, "7 months", height=167, weight = 60)
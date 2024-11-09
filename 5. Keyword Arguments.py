#Positional arguments can cause the alternate result
#We can tackle this issue with keyword arguments
def display(name, age):
    print(f"Hello. My name is {name} and I am {age} years old.")
display(age=29, name="Naresh")  #bad practice as it will make code longer
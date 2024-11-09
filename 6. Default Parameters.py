def display(name="Naresh", age=29):
    print(f"Hello. My name is {name} and I am {age} years old.")
display()   #This will print the result as parameters are already defined as default

#Even we can call new function with new arguments
display("Uma",28)

#If we fill only one argument, it will act as positional and print accordingle
display("Mahadev")  #Age will print out automatically from default parameters
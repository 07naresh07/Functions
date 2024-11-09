def count():
    total = 0
    total += 1
    return total

count()
count()
print(count())

#since total is local variable, once the count() function is called it returns 1
#When count() is called next time, it returns 1 as total will reset to 0 once function call is over
#If function is called next time, local variable will set to the defined value
#This is because the scope of local variable

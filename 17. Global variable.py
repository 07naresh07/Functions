total = 0
def count():
    global total
    total+=1
    return total

count()
count()
print(count())
#First count will return total=1, this will set the global total=1
#Second count will be 2 as total as a global variable is assigned to 1 from first call of function
#Third count will give 3 as output
#Global variables has tendency to change once they are called
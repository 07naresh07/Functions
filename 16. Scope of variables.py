#variable in python has limited scope except global variables. Following are the order or rules of variables
'''
1. Local: checks with in the local range
2. Parent: if there is no variable in local, checks in parent range
3. Global: If not in both local and parent, uses global variable
4. Build in python functions: Functions like sum(4,5) or similar kind of functions that can be used
'''
a=10    #Global variable
def parent():
    a=15    #Parent variable
    def child():
        return a    #There is no local variable defined in child(), so it sets a=15
    return child()
print(parent())
print(a)    #Access global variable i.e. a=10


picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
def christmasTree():
    for image in picture:
        for pixel in image:
            if pixel==0:
                print(" ", end="")  #By default print() ends with "\n", and to override newline, "" is used
            else:
                print("*", end="")
        print("",end="\n")  #By default print function ends with print(end="\n") and to overcome this \n, we have to use "" to print in same line
i = 0
while i<=5:
    christmasTree()
    i+=1

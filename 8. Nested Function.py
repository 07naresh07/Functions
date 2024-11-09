def sum(num1, num2):
    def anotherSum(n1, n2):
        return n1+n2
    return anotherSum(num1, num2)
#If function is returned with return, we are automatically exiting out of the function, it will not print anything below return

print(sum(10,23))
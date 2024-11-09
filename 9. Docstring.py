#Docstring: is typically enclosed between '''*''' and it is mainly used for storing information about what function is used for
def test(name, age):
    '''
    This function is used for printing name and age of the applicant.
    '''
    print(f"{name}, {age}")

test("Naresh",29)
#If we use help() function, it will give the information written in ''' '''
help(test)
#OR
print(test.__doc__)
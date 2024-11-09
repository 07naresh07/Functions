total = 0
def count(total):
    total += 1
    return total

print(count(count(count(total))))

#This will give the result as 3
#Result start with first count(total) and gives 1, which will be passed to next count(count(1)) and gives 2 and finally 3.
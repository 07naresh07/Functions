def highestEven(data):
    evens = []
    for item in data:
        if item%2==0:
            evens.append(item)
    return max(evens) if evens else None

print(highestEven([13, 4, 3, 6, 9, 14, 19, 16]))
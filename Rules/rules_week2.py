# classic rules
points = [1,4,9,16,25,36,49,64,81,100]
def battle(left,right):
    if left > right:
        return 1
    elif left < right:
        return 2
    else:
        return 0

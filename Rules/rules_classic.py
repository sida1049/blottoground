# classic rules
points = [1,2,3,4,5,6,7,8,9,10]
def battle(left,right):
    if left > right:
        return 1
    elif left < right:
        return 2
    else:
        return 0

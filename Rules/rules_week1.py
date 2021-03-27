# Week 1: domination
# Player wins a tower if their soldiers there at least double their opponents'
points = [1,2,3,4,5,6,7,8,9,10]
def battle(left,right):
    if left >= 2*right:
        return 1
    elif 2*left <= right:
        return 2
    else:
        return 0

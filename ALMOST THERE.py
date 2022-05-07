#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True

#NOTE: abs(num) returns the absolute value of a number
def almost_there(n):
    if n in range (90, 110):
        return True
    elif n in range (190,210):
        return True
    else:
        return False

    return (abs(100 - n) <= 10) or (abs (200 - n) <= 10)



print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

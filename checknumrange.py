#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low,high):
        return f"{num} is within range {low} and {high}"


print(ran_check(5,2,7))
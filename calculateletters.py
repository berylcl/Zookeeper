#Write a Python function that accepts a string and calculates
#the number of upper case letters and lower case letters.

def up_low(s):
    uppercase = 0
    lowercase = 0
    for char in s:
        if char.isupper():
            uppercase+=1
        elif char.islower():
            lowercase+=1
        else:
            pass
        print(f"Original string:{s}")
        print(f"Lowercase count:{lowercase}")
        print(f"Uppercase count::{uppercase}")


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))





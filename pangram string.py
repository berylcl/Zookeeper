#Write a Python function to check whether a string is pangram or not.
# (Assume the string passed in does not have any punctuation)
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(" ", '')
    alphaset = set(alphabet)
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset




print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("The job requires extra pluck and zeal from every young wage earner. "))
print(ispangram("Waltz, bad nymph, for quick jigs vex"))
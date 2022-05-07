#Write a Python function that checks whether a word or phrase is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads
#the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run".

def palindrome(s):
    #Remove spaces from string
    s = s.replace(' ', '')
    if s == s[::-1]:
        return True
    else:
        return False

print(palindrome('helleh'))
print(palindrome('nurses run'))

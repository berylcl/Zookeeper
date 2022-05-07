#Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    wordlist = text.split()
    if wordlist[0][0].upper() == wordlist[1][0].upper():
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print(animal_crackers('Crazy Cat'))
#Write a function that capitalizes the first and fourth letters of a name
#old_macdonald('macdonald') --> MacDonald
def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return first_letter.capitalize() + inbetween + fourth_letter.capitalize() + rest




print(old_macdonald('macdonald'))
#Write a function that capitalizes the first and fourth letters of a name
#old_macdonald('macdonald') --> MacDonald
def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()


print(old_macdonald('macdonald'))
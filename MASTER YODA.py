#Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    new_list = text.split()
    reversed_list = new_list[::-1]
    return " ".join(reversed_list)


print(master_yoda('I am home'))
print(master_yoda('We are ready'))
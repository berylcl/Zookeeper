class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book('Kintu','Jeniffer Nasumbuga', 440)
print(b)
print(len(b))


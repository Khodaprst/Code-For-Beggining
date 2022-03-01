class Book:
    def __init__(self, title, author, pages):
        print('Book has been created')
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'title: {}, Author: {}, Pages: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def setter():
        pass

    def getter():
        pass

ketab = Book('Python', 'AmirHosein', 300)
print(len(ketab))

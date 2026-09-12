class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    def __repr__(self):
        status = "امانت داده شده" if self.is_borrowed else "موجود"
        return f"{self.title} - {self.author} (ISBN: {self.isbn}) ({status}) "

    def borrow(self):
        if self.is_borrowed:
            raise ValueError("کتاب امانت داده شده ")
        self.is_borrowed = True
    def return_book(self):
        if  not self.is_borrowed:
            raise ValueError("این کتاب امانت داده نشده ")
        self.is_borrowed = False 
    def to_dict(self):
       return {
            "title":self.title,
            "author":self.author,
            "isbn":self.isbn,
            "is_borrowed":self.is_borrowed
        }
    @classmethod
    def from_dict(cls,data):
        book = cls(data["title"], data["author"], data["isbn"])
        book.is_borrowed = data["is_borrowed"]
        return book

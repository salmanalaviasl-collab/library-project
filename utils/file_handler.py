from models.book import Book
import json

def save_books(books, filepath):
    data = [book.to_dict() for book in books]
    with open(filepath,"w",encoding="utf-8") as f :
        json.dump(data,f,ensure_ascii=False, indent=4)
    
def load_books(filepath):
    with open(filepath,"r",encoding="utf-8") as f :
        raw_data = json.load(f)
        books =[Book.from_dict(item) for item in raw_data]
    return books

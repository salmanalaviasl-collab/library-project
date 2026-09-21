from django.shortcuts import render 
from .models import Book
def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html",{"books":books})
def book_detail(requset,book_id):
    book = Book.objects.get(id= book_id)
    return render(requset,"library/book_detail.html",{'book': book})
# Create your views here.

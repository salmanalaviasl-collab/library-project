from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
def book_list(request):
    books = Book.objects.all()
    return render(request,"library/book_list.html",{"books": books})
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "library/add_book.html", {"form": form})
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("book_list")
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, 'library/edit_book.html',{"form":form})

        
# Create your views here.

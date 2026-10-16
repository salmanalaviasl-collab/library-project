from django.shortcuts import render, redirect
from .models import Book, Loan, Member
from .forms import BookForm, LoanForm, MemberForm
from django.contrib.auth.decorators import login_required

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request,"library/book_list.html",{"books": books})
@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "library/add_book.html", {"form": form})
@login_required
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("book_list")
@login_required
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
@login_required
def loan_book(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.book = book 
            loan.save()
            return redirect('book_list')
    else:
        form = LoanForm()
    return render(request, 'library/loan_book.html' , {'form':form})
@login_required
def book_detail(request,book_id):
    book = Book.objects.get(id=book_id)
    loans = Loan.objects.filter(book=book)
    return render(request,'library/book_detail.html',{"book":book , "loans":loans })
@login_required
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request,'library/add_member.html',{'form':form})
@login_required
def member_list(request):
    members = Member.objects.all()
    return render(request,'library/member_list.html',{'members':members})
@login_required
def delete_member(request,member_id):
    member = Member.objects.get(id=member_id)
    member.delete()
    return redirect('member_list')
@login_required
def edit_member(request,member_id):
    member = Member.objects.get(id=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request,'library/edit_member.html',{'form':form})
@login_required
def return_book(request,loan_id):
    loan = Loan.objects.get(id=loan_id)
    loan.is_returned = True
    loan.save()
    return redirect('book_detail', book_id=loan.book.id)
@login_required
def member_detail(request, member_id):
    member = Member.objects.get(id=member_id)
    loans = Loan.objects.filter(member=member)
    return render(request, 'library/member_detail.html',{'member':member,'loans':loans})




    



        
# Create your views here.

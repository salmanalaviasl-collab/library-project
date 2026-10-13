from django import forms 
from .models import Book, Loan
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "total_copies"]
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["member", "borrow_date"]
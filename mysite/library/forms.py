from django import forms 
from .models import Book, Loan, Member
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "total_copies"]
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["member", "borrow_date"]
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']
        


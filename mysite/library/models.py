from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author= models.CharField(max_length=100)
    total_copies = models.IntegerField(default=1)
    def available_copies(self):
        active_loans = Loan.objects.filter(book=self, is_returned=False).count()
        return self.total_copies - active_loans
    def __str__(self):
        return self.title
class Member(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    is_returned = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.member.name} - {self.book.title}"
    

# Create your models here.

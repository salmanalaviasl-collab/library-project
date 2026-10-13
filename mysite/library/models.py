from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author= models.CharField(max_length=100)
    total_copies = models.IntegerField(default=1)
    def available_copies(self):
        borrowed_count = Loan.objects.filter(book=self).count()
        return self.total_copies - borrowed_count
    def __str__(self):
        return self.title
class Member(models.Model):
    name = models.CharField(max_length=100)
class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    def __str__(self):
        return f"{self.member.name} - {self.book.title}"
    

# Create your models here.

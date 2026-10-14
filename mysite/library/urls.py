from django.urls import path
from . import views
urlpatterns = [
    path("",views.book_list, name="book_list"),
    path("add/", views.add_book, name="add_book"),
    path('<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path("<int:book_id>/edit/" , views.edit_book, name="edit_book"),
    path("<int:book_id>/loan/", views.loan_book, name="loan_book"),
    path("<int:book_id>/detail/",views.book_detail, name="book_detail")

]
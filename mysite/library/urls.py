from django.urls import path
from . import views
urlpatterns = [
    path("",views.book_list, name="book_list"),
    path("add/", views.add_book, name="add_book"),
    path('<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path("<int:book_id>/edit/" , views.edit_book, name="edit_book"),
    path("<int:book_id>/loan/", views.loan_book, name="loan_book"),
    path("<int:book_id>/detail/",views.book_detail, name="book_detail"),
    path("member/",views.member_list,name='member_list'),
    path("member/add/", views.add_member, name ='add_member'),
    path("member/<int:member_id>/edit/",views.edit_member, name='edit_member'),
    path("member/<int:member_id>/delete/",views.delete_member, name='delete_member'),
    path("loan/<int:loan_id>/return/", views.return_book, name='return_book'),
    path("member/<int:member_id>/detail/",views.member_detail,name='member_detail')


]
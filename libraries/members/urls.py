from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:book_id>/', views.book_availability, name = 'book_availability'),
    path('member-login/' , views.member_entry, name = 'members'),
]
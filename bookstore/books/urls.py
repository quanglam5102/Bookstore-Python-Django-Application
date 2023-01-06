from django.urls import path
# Import views from current base app folder
from . import views

# Create base app urls
urlpatterns = [
    # Route for login page
    path('login/', views.loginPage, name="login"),
    # Route for login page
    path('logout/', views.logoutUser, name="logout"),
    # Route for register page
    path('register/', views.registerUser, name="register"),

    #Book Routes
    path('', views.books, name="books"),
    path('book/<str:pk>/', views.book, name="book"),
    path('queryBook/', views.queryBook, name="book"),
    path('addBook/', views.addBook, name="addBook"),
    path('editBook/<str:pk>/', views.editBook, name="editBook"),
    path('deleteBook/<str:pk>/', views.deleteBook, name="deleteBook"),
]
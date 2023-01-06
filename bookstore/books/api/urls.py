# Import path
from django.urls import path
# Import api views
from . import views

# Define API routes
urlpatterns = [
    path('',  views.getRoutes),
    path('books/', views.getBooks),
    path('book/<str:pk>/', views.getBook),
]

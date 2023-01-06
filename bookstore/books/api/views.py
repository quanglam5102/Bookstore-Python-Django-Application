# Import decorator for api view from DRF
from rest_framework.decorators import api_view
# Import Response from DRF
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def getRoutes(request):
    allRoutes = [
        'GET /api',
        'GET /api/books',
        'GET /api/book/:id'
    ]
    return Response(allRoutes)


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

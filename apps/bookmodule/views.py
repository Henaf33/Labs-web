from django.shortcuts import render

# قائمة الكتب (ديناميكية)
books = [
    {'id': 1, 'title': 'Internet & WWW How to Program', 'author': 'Paul Deitel', 'image': 'book1.jpg', 'description': 'Learn web development.'},
    {'id': 2, 'title': 'C++ How to Program', 'author': 'Paul Deitel', 'image': 'book2.jpg', 'description': 'Master C++ programming.'},
    {'id': 3, 'title': 'Python Crash Course', 'author': 'Eric Matthes', 'image': 'book3.jpg', 'description': 'A fast-paced Python guide.'}
]

def index(request):
    return render(request, "bookmodule/index.html", {"books": books})

def list_books(request):
    return render(request, "bookmodule/list_books.html", {"books": books})

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def viewbook(request, bookId):
    book = next((b for b in books if b['id'] == bookId), None)
    return render(request, "bookmodule/one_book.html", {"book": book})

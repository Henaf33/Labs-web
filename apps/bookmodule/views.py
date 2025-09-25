from django.http import HttpResponse
from django.shortcuts import render


# الدالة الأولى - تستخدم قالب HTML وتعرض متغير name
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

# الدالة الثانية - تعرض قيمة val1 مباشرة باستخدام HttpResponse
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    # افترض أن هذه الكتب موجودة (يمكن لاحقًا من قاعدة بيانات)
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}  # هذا المتغير سيكون متاحًا في القالب
    return render(request, 'bookmodule/show.html', context)

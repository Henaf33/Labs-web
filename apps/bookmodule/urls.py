from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # الصفحة الرئيسية للتطبيق
    path('index2/<int:val1>/', views.index2),  # view الثانية مع باراميتر
    path('<int:bookId>/', views.viewbook),  # رابط لعرض تفاصيل كتاب بالرقم

]


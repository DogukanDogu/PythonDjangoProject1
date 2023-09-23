from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('<int:num>/',views.course_number,name="Course Number View"),
    path('<str:item_course>/',views.course,name="course"),
]
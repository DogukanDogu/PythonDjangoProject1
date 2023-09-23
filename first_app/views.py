from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

course_dictionary = {
    "python" : "Python Course Page",
    "java" : "java Course Page",
    "kotlin" : "Kotlin First Page",
    "swift" : "Swift First Page",
}

def index(request):
    return HttpResponse("This is first Django Project Index")

def course(request,item_course):
    try:
        course = course_dictionary[item_course]
        return HttpResponse(course)
    except:
        raise(Http404("Not Found!!!"))
    
def course_number(request,num):
    course_list = list(course_dictionary.keys())
    course = course_list[num]

    page_to_go = reverse("course",args=[course])
    
    return HttpResponse(page_to_go)

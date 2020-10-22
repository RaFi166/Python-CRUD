from django.shortcuts import render
from django.http import HttpResponse
from first_app import forms

# Create your views here.
def index(request):
    main_form=forms.Student()
    dictionary={'form_here':main_form}
    if request.method=="POST":
        main_form=forms.Student(request.POST)

        if main_form.is_valid():
            main_form.save(commit=True)



    return render (request,"first_app/index.html",context=dictionary)

def student_form(request):
    return render(request,"first_app/base.html")
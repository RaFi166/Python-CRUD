from django.shortcuts import render
from django.http import HttpResponse
from first_app import forms
from first_app.models import StudentForm

# Create your views here.
def index(request):
    main_form=forms.Student()
    dictionary={'form_here':main_form, 'title':"Index"}
    if request.method=="POST":
        main_form=forms.Student(request.POST)

        if main_form.is_valid():
            main_form.save(commit=True)



    return render (request,"first_app/index.html",context=dictionary)

def student(request):
    all_students= StudentForm.objects.all()
    diction={'title':"Students", 'students':all_students}

    return render(request,"first_app/students.html", context=diction)

def student_info(request,student_id):
    student_info=StudentForm.objects.get(pk=student_id)
    diction={'student_info':student_info}
    return render (request,"first_app/students_info.html", context=diction )

def info_edit(request,student_id):

    student_data=StudentForm.objects.get(pk=student_id)

    student_form=forms.Student(instance=student_data)
    diction={'student':student_form}

    if request.method=="POST":
        student_form=forms.Student(request.POST,instance=student_data)
        if student_form.is_valid():
            student_form.save(commit=True)
            
    return render (request,"first_app/info_edit.html",context=diction)
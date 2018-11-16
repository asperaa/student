from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm


# Create your views here.

def student_list(request):       #function to extract all the student data from database
    students = Student.objects.all()
    return render(request, 'student_info/student_list.html', {'students':students})


def add_student(request):       #function to add a new student information into a database
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('/', pk=post.pk)
    else:
        form = StudentForm()
        return render(request,'student_info/student_form.html',{'form':form})
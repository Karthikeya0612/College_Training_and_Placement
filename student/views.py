from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def add_student(request):
    students_to_delete = Student.objects.filter(rollno='20881A1203')
    students_to_delete.delete()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form':form})
    
def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students':students})

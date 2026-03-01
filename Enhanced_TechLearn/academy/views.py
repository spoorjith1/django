from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Trainer, Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def courses_page(request):
    CourseData = Course.objects.all()
    context = {
        'courses' : CourseData,
    } 
    return render(request, 'courses.html', context)


def trainers_page(request):
    TrainerData = Trainer.objects.all()
    context = {
        'trainers' : TrainerData,
    } 
    return render(request, 'trainers.html', context)


def students_page(request):
    StudentData = Student.objects.all()
    context = {
        'students' : StudentData,
    } 
    return render(request, 'students.html', context)


@login_required
@permission_required('academy.add_student', raise_exception=True)
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:
            print(form.errors)
    form = StudentForm()
    context = {
        'form': form
    }
    return render(request, "add_student.html", context)


def trainer_details(request, id):
    trainerData = get_object_or_404(Trainer, id=id)
    context = {
        'trainer' : trainerData,
    }
    return render(request, 'cruds/trainer_details.html', context)


def trainer_edit(request, id):
    if request.method == "POST":
        Data = get_object_or_404(Trainer, id=id)
        Data.first_name = request.POST.get('first_name')
        Data.last_name = request.POST.get('last_name')
        Data.email = request.POST.get('email')
        Data.save()
        return redirect('trainers')
    else:
        Data = get_object_or_404(Trainer, id=id)
    context = {
        'trainerData' : Data,
    }
    return render(request, 'cruds/trainer_edit.html', context)


def student_details(request, id):
    studentData = get_object_or_404(Student, id=id)
    context = {
        'student': studentData,
    }
    return render(request, 'cruds/student_details.html', context)


def student_edit(request, id):
    if request.method == "POST":
        Data = get_object_or_404(Student, id=id)
        Data.first_name = request.POST.get('first_name')
        Data.last_name = request.POST.get('last_name')
        Data.email = request.POST.get('email')
        Data.save()
        return redirect('students')
    else:
        Data = get_object_or_404(Student, id=id)
    context = {
        'studentData' : Data,
    }
    return render(request, 'cruds/student_edit.html', context)


@login_required
@permission_required('academy.delete_student', raise_exception=True)
def student_delete(request, id):
    std = get_object_or_404(Student, id=id)
    if request.method == "POST":
        std.delete()
        return redirect('students')
    context = {
        'student': std
    }
    return render(request, 'cruds/student_del.html', context)
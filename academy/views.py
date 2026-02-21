from django.shortcuts import render
from .models import Course, Trainer, Student
# Create your views here.

def courses_page(request):
    CourseData = Course.objects.all()
    context = {
        'courses' : CourseData,
    } 
    return render(CourseData, 'courses.html', context)

def trainers_page(request):
    TrainerData = Trainer.objects.all()
    context = {
        'trainers' : TrainerData,
    } 
    return render(TrainerData, 'trainers.html', context)

def students_page(request):
    StudentData = Student.objects.all()
    context = {
        'students' : StudentData,
    } 
    return render(StudentData, 'students.html', context)
from django.shortcuts import render
from academy.models import Course, Trainer, Student

def home(request):
    CourseData = Course.objects.all()
    TrainerData = Trainer.objects.all()
    StudentData = Student.objects.all()
    total_students = Student.objects.count()
    context = {
        'courses' : CourseData,
        'trainers' : TrainerData,
        'students' : StudentData,
        'studentsCount' : total_students,
    }
    return render(request, "home.html", context)
from django.urls import path
from .views import courses_page, trainers_page, students_page

urlpatterns = [
    path('courses/', courses_page, name="courses"),
    path('trainers/', trainers_page, name="trainers"),
    path('students/', students_page, name="students")
]
from django.urls import path
from .views import courses_page, trainers_page, students_page, add_student, trainer_details, trainer_edit, student_details, student_edit, student_delete

urlpatterns = [
    path('courses/', courses_page, name="courses"),
    path('trainers/', trainers_page, name="trainers"),
    path('students/', students_page, name="students"),
    path('addStudent/', add_student, name="AddStudent"),
    path('<int:id>/trainerdetails/', trainer_details, name="TrainerD"),
    path('<int:id>/traineredit/', trainer_edit, name='TrainerE'),
    path('<int:id>/stddetails/', student_details, name="StudentD"),
    path('<int:id>/stdedit/', student_edit, name='StudentE'),
    path('<int:id>/stddelete', student_delete, name='DelStd'),
]
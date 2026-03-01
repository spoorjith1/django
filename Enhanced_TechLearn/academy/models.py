from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    duration = models.CharField()
    
    def __str__(self):
        return f"{self.course_name}"
 
class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    expertise = models.ForeignKey(Course, on_delete=models.PROTECT)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.full_name()} - {self.expertise}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    enrolled_course = models.ForeignKey(Course, on_delete=models.PROTECT)
    trainer = models.ForeignKey(Trainer, on_delete=models.PROTECT)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.full_name()} | {self.enrolled_course} - {self.trainer}"
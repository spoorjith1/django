from django.contrib import admin
from .models import Course, Trainer, Student

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'description', 'duration']
    list_display_links = ["course_name"]
    search_fields = ["course_name"]
    list_editable = ["description"]
    ordering = ["id"]

class TrainerAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'expertise']
    list_display_links = ["expertise", "full_name"]
    search_fields = ["expertise"]
    ordering = ["id"]
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id' ,'full_name', 'email', 'is_active', 'enrolled_course', 'trainer']
    list_filter = ["enrolled_course"]
    list_display_links = ["full_name"]
    list_editable = ["is_active", "enrolled_course", "trainer"]
    search_fields = ["full_name", "enrolled_course", "trainer"]
    ordering = ["id"]


admin.site.register(Course, CourseAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Student, StudentAdmin)
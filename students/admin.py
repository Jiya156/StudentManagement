from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ("Name","Email","Roll_Number","Course","Semester","Batch")

admin.site.register(Student,StudentAdmin)

# Register your models here.

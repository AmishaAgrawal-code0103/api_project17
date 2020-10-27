from django.contrib import admin
from testapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    '''
        Admin View for Student
    '''
    list_display = ('sname', 'semail', 'sphone_no', 'saddress',)

admin.site.register(Student, StudentAdmin)

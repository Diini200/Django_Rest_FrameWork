from django.contrib import admin

from testApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id','emp_number','emp_name','emp_salary', 'emp_address']
    
admin.site.register(Employee, EmployeeAdmin)
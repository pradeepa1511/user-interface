from django.contrib import admin
from Regapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['No','Name','Mob','Purpose_of_entry','Person_to_be_met']
admin.site.register(Student,StudentAdmin)
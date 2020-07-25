from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['No',
            'Name',
            'Mob',
            'Purpose_of_entry',
            'Person_to_be_met',
		]
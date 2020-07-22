from django.db import models

# Create your models here.
class Student(models.Model):
	No = models.IntegerField()
	Name = models.CharField(max_length=25)
	Mob = models.IntegerField()
	Purpose_of_entry = models.CharField(max_length=64)
	Person_to_be_met = models.CharField(max_length=25)



    


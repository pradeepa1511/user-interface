from django.db import models

# Create your models here.
class Staff(models.Model):
    studentsaccceptorreject=models.CharField(max_length=10,default='accept')

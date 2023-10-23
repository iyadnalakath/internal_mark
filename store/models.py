from django.db import models
from projectaccount.models import Semester

# Create your models here.

class Student(models.Model):
    semester = semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE, related_name="student_semester", null=True, blank=True
    )
    name = models.CharField(max_length=50,null=True,blank=True)
    register_number = models.IntegerField(null=True,blank=True)
    roll_number = models.IntegerField(null=True,blank=True)


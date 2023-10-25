from django.db import models
from projectaccount.models import Semester,Subject

# Create your models here.

class Student(models.Model):
    semester = semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE, related_name="student_semester", null=True, blank=True
    )
    name = models.CharField(max_length=50,null=True,blank=True)
    register_number = models.IntegerField(null=True,blank=True)
    roll_number = models.IntegerField(null=True,blank=True)


class TheoryInternalMark(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="student_name", null=True, blank=True
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="Theory_subject", null=True, blank=True
    )
    se1 = models.IntegerField(null=True,blank=True)
    se2 = models.IntegerField(null=True,blank=True)
    se3 = models.IntegerField(null=True,blank=True)
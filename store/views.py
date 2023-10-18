from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from projectaccount.models import Account, Subject,Semester
from store.models import Student
from store.serializer import RegisterStudentSerializer, RegisterTeacherSerializer, SemesterSerializer, SubjectSerializer

# Create your views here.


class SubjectViews(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



class SemesterViews(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer



class TeacherRegistrationView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    # queryset = Account.objects.all()
    serializer_class = RegisterTeacherSerializer

    def get_queryset(self):
        return Account.objects.filter(role="teacher")

class StudentRegistrationView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = RegisterStudentSerializer


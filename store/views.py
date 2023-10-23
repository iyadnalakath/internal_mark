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

    # def list(self, request, *args, **kwargs):
    #         queryset = self.get_queryset()

    #         if self.request.user.role == "teacher":
    #             if self.request.GET.get("exam_name"):
    #                 exam_name = self.request.GET.get("exam_name")
    #                 queryset = queryset.filter(exam_name=exam_name)

    #             queryset = queryset.filter(teacher=self.request.user.id)
    #             serializer = QuestionsSerializer(
    #                 queryset, many=True, context={"request": self.request}
    #             )
    #             return Response(serializer.data, status=status.HTTP_200_OK)

    #         else:
    #             return super().list(request, *args, **kwargs)
            
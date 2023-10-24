from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from projectaccount.models import Account, Subject,Semester
from store.models import Student
from store.serializer import RegisterStudentSerializer, RegisterTeacherSerializer, SemesterSerializer, SubjectSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class SubjectViews(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def list(self, request, *args, **kwargs):
        if self.request.user.role == "teacher":
            # If the user is a teacher, filter subjects by the teacher's associated subjects.
            queryset = self.request.user.subject.all()
        else:
            # If not a teacher, return all subjects.
            queryset = self.get_queryset()

        serializer = SubjectSerializer(
            queryset, many=True, context={"request": self.request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class SemesterViews(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


    def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()

            if self.request.user.role == "teacher":
                # if self.request.GET.get("exam_name"):
                    # exam_name = self.request.GET.get("exam_name")
                # queryset = queryset.filter(exam_name=exam_name)

                queryset = queryset.filter(name=self.request.user.subject__semester.name)
                serializer = SemesterSerializer(
                    queryset, many=True, context={"request": self.request}
                )
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return super().list(request, *args, **kwargs)
          



class TeacherRegistrationView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    # queryset = Account.objects.all()
    serializer_class = RegisterTeacherSerializer

    def get_queryset(self):
        return Account.objects.filter(role="teacher")


class StudentRegistrationView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    # queryset = Student.objects.all()
    serializer_class = RegisterStudentSerializer

    def get_queryset(self):
        semester_id = self.request.query_params.get('semester_id')

        if semester_id:
            return Student.objects.filter(semester_id=semester_id)

        return Student.objects.all()


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
            
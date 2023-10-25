from rest_framework import serializers
from projectaccount.models import Account, Subject ,Semester
from .models import LabInternalMark, Student, TheoryInternalMark



class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('id', 'name')

class SubjectSerializer(serializers.ModelSerializer):
    # semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all(), many=True)
    semester_name = serializers.CharField(source="semester.name", read_only=True)

    class Meta:
        model = Subject
        fields = ('id', 'name','semester','semester_name','role')
    


class RegisterTeacherSerializer(serializers.ModelSerializer):
    # subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    # subject_name = serializers.CharField(source="subject.name", read_only=True)
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True)
    subject_name = serializers.StringRelatedField(source="subject", many=True, read_only=True)

    password = serializers.CharField(write_only=True)
    copy_pass = serializers.CharField(read_only=True)
    
    class Meta:
        model = Account
        fields = ["id", "full_name", "username", "password", "subject", "subject_name", "copy_pass"]
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
        }

    def create(self, validated_data):
        subject = validated_data.pop('subject', None)
        # semester = validated_data.pop('semester', None)
        password = validated_data.pop('password')  
        user = Account.objects.create(
            username=validated_data["username"],
            full_name=validated_data["full_name"],
            role="teacher",
            copy_pass=password,  # Set copy_pass here
        )
        user.set_password(password)  

        # if subject:
        #     user.subject = subject

        if subject:
            user.subject.set(subject)  # Set multiple semesters

        
        user.save()

        return user

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['copy_pass'] = instance.copy_pass  # Include copy_pass in the response
        return ret
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['subject_name'] = [subject.name for subject in instance.subject.all()]
        return ret

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['copy_pass'] = instance.copy_pass  # Include copy_pass in the response
    #     return ret


class RegisterStudentSerializer(serializers.ModelSerializer):

    semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all())
    semester_name = serializers.CharField(source="semester.name", read_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "register_number",
            "roll_number",
            "semester",
            "semester_name"
        ]

class TheoryInternalMarkSerializer(serializers.ModelSerializer):
    student_name = RegisterStudentSerializer(source="student",read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    average_internal_mark = serializers.SerializerMethodField()
    average_assignment_mark = serializers.SerializerMethodField()
    
    attendance_percentage_mark = serializers.SerializerMethodField()

    class Meta:
        model = TheoryInternalMark
        fields = [
            "id",
            "student",
            "student_name",
            "subject",
            "subject_name",
            "semester",
            "se1",
            "se2",
            "se3",
            "average_internal_mark", 

            "assignment1",
            "assignment2",
            "assignment3",
            "average_assignment_mark",

            "attendance_percentage",
            "attendance_percentage_mark"
        ]

    def get_average_internal_mark(self, obj):
        se1 = obj.se1 or 0
        se2 = obj.se2 or 0
        se3 = obj.se3 or 0

        total_marks = se1 + se2 + se3
        return total_marks / 3
    

    def get_average_assignment_mark(self, obj):
        assignment1 = obj.assignment1 or 0
        assignment2 = obj.assignment2 or 0
        assignment3 = obj.assignment3 or 0

        total_marks = assignment1 + assignment2 + assignment3
        return total_marks / 3
    
    def get_attendance_percentage_mark(self, obj):
        attendance_percentage = obj.attendance_percentage

        if attendance_percentage is not None:
            if 90 <= attendance_percentage <= 100:
                return 10
            elif 80 <= attendance_percentage < 90:
                return 9
            elif 70 <= attendance_percentage < 80:
                return 8
            elif 60 <= attendance_percentage < 70:
                return 7
            else:
                return 6
        else:
            return 0



class LabInternalMarkSerializer(serializers.ModelSerializer):

    student_name = RegisterStudentSerializer(source="student",read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    average_test_mark = serializers.SerializerMethodField() 

    class Meta:
        model = LabInternalMark
        fields = [
            
            'id',
            "student",
            "student_name",
            "subject",
            "subject_name",
            "semester",

            "test1",
            "test2",
            "average_test_mark",

            "rough_record_mark",
            "fair_record_mark",
            "lab_work_mark",
            "open_ended_mark",
            "attendance_mark"

            ]
        
    def get_average_test_mark(self, obj):
        test1 = obj.test1 or 0
        test2 = obj.test2 or 0

        total_marks = test1 + test2
        return total_marks / 2
    
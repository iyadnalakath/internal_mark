from rest_framework import serializers
from projectaccount.models import Account, Subject ,Semester
from .models import Student


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')
    

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('id', 'name')
    

class RegisterTeacherSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all())
    semester_name = serializers.CharField(source="semester.name", read_only=True)
    password = serializers.CharField(write_only=True)
    copy_pass = serializers.CharField(read_only=True)

    class Meta:
        model = Account
        fields = ["id", "full_name", "username", "password", "subject", "subject_name", "copy_pass","semester","semester_name"]
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
        }

    def create(self, validated_data):
        subject = validated_data.pop('subject', None)
        semester = validated_data.pop('semester', None)
        password = validated_data.pop('password')  
        user = Account.objects.create(
            username=validated_data["username"],
            full_name=validated_data["full_name"],
            role="teacher",
            copy_pass=password,  # Set copy_pass here
        )
        user.set_password(password)  

        if subject:
            user.subject = subject

        if semester:
            user.semester = semester
        
        user.save()

        return user

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['copy_pass'] = instance.copy_pass  # Include copy_pass in the response
        return ret

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['copy_pass'] = instance.copy_pass  # Include copy_pass in the response
    #     return ret


class RegisterStudentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "register_number",
            "roll_number"
        ]

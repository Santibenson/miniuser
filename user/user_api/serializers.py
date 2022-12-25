from rest_framework import serializers
from user.models import User, Student, Teacher


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'is_teacher', 'is_student']


class StudentSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error':'Password does not match'})
        user.set_password(password)
        user.is_student = True
        user.save()
        Student.objects.create(
            user=user,
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email
        )
        return user

class TeacherSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error':'Password does not match'})
        user.set_password(password)
        user.is_teacher = True
        user.save()
        Teacher.objects.create(
            user=user,
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email
            )
        return user
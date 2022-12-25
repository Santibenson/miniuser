from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models
from datetime import datetime


from rest_framework.authtoken.models import Token


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def generate_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Student(models.Model):
    user = models.OneToOneField(User, limit_choices_to={
                                'is_student': True}, related_name='student', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    reg_number = models.CharField(max_length=10, blank=True, null=True)
    short_bio = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    hobbies = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Teacher(models.Model):
    user = models.OneToOneField(User, limit_choices_to={
                                'is_teacher': True}, related_name='teacher', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    short_bio = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    hobbies = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

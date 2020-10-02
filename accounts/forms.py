from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Student, User,Teacher

class StudentSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone=forms.CharField(required=True)
    desination=forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.phone=self.cleaned_data.get('phone')
        teacher.desination=self.cleaned_data.get('desination')
        teacher.save()

        return teacher
from .models import Student_Admission
from django.forms import ModelForm


class Student_admission_form(ModelForm):
    class Meta:
        model = Student_Admission
        fields = ['name', 'father_name', 'mother_name',
                  'email', 'number', 'student_image']

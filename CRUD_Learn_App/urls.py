from django.urls import path
from .views import student_admission, index, student_list, Student_details, student_update, Student_delete

urlpatterns = [
    path('', index, name='main'),
    path('admission_form/', student_admission, name='student_admission'),
    path('student_list/', student_list, name='student_list'),
    path('student_details/<int:id>/', Student_details, name='Student_details'),
    path('student_update/<int:id>/', student_update, name='student_update'),
    path('student_delete/<int:id>/', Student_delete, name='Student_delete')
]

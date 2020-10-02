from django.urls import path
from .views import SingUp,StudentSignUpView,TeacherSignUpView
urlpatterns = [
path('singup/',SingUp,name='singup'),
  path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
  path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
]
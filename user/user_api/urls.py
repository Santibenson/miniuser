from django.urls import path
from .views import StudentSignUpView, TeacherSignUpView, CustomAuthToken

urlpatterns = [
    path('signup/student', StudentSignUpView.as_view()),
    path('signup/teacher', TeacherSignUpView.as_view()),
    path('login',CustomAuthToken.as_view())
]

from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import question_new,question_list,question_detail,paper_new,RegisterStudent,verify,student_home,logout_user

urlpatterns = [
    path('login/', verify, name='login'),
    path('logout/', logout_user, name='logout'),
    path('student/', student_home, name='student_home'),
    path('admin/', TemplateView.as_view(template_name='admin_home.html'), name='admin_home'),
    path('teacher/', TemplateView.as_view(template_name='teacher_home.html'), name='teacher_home'),
    path('register/student/', RegisterStudent, name='student_register'),
    path('question/all/', question_list, name='question_list'),
    path('question/<int:pk>/', question_detail, name='question_detail'),
    path('question/new/', question_new, name='question_new'),
    path('paper/new',paper_new, name='paper_new')
]
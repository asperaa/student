from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/new/',views.add_student,name='add_student')
]

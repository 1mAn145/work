from django.urls import path
from apps.course.views import create_course, course_detail, task

urlpatterns = [
    path('create_course/',create_course, name="create_course"),
    path('course_detail/<int:id>/',course_detail ,name='course_detail'),
    path('task/<int:id>',task,name='task_detail'),

]
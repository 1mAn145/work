from apps.course.models import Course
from django.forms import ModelForm

class CreateCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title','image','direction','subject']
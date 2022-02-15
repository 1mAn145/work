from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from apps.course.models import Course, Tasks


admin.site.register(Course)
admin.site.register(Tasks)


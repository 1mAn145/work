from django.urls import reverse
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE,blank=True)
    title = models.CharField(max_length=55, verbose_name="Название",blank=True)
    image = models.ImageField(blank=True,upload_to='images/',verbose_name="Загрузите фото")
    direction = models.CharField(max_length=55,verbose_name="Напровление",blank=False,null=True)
    subject =models.CharField(max_length=55,verbose_name="Предмет",blank=True, default='Предмет')
    
    
    class Meta:
        verbose_name_plural="Курсы"
        verbose_name = "Курс"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'id': self.id, 'name': self.name})

class Tasks(models.Model):
    course=models.ForeignKey(Course, related_name='course_tasks',on_delete=CASCADE,blank=True,null=True)
    title = models.CharField(max_length=55,verbose_name='Название')
    task = models.CharField(max_length=255,verbose_name='Инструкция')
    date = models.DateField(verbose_name='Дата',auto_now_add=False, blank=True, null=True)
    points = models.IntegerField(verbose_name="Баллы",null=True,blank=True)
    
    class Meta:
        verbose_name_plural= "Задания"
        verbose_name = "Задание"
    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'id': self.id, 'name': self.name})
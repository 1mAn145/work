# Generated by Django 3.2.9 on 2022-01-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_rename_logo_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

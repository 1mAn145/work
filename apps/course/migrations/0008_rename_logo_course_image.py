# Generated by Django 3.2.9 on 2022-01-10 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='logo',
            new_name='image',
        ),
    ]
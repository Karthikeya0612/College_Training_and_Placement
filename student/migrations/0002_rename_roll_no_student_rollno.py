# Generated by Django 4.2.3 on 2023-07-16 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll_no',
            new_name='rollno',
        ),
    ]
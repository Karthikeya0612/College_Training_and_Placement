# Generated by Django 4.2.3 on 2023-07-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('section', models.CharField(max_length=10)),
            ],
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-14 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Register_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('Enrollment_No', models.CharField(max_length=120)),
                ('Ph_No', models.CharField(max_length=120)),
                ('CGPA', models.CharField(max_length=120)),
                ('Percentage_in_10th', models.CharField(max_length=120)),
                ('Percentage_in_12th', models.CharField(max_length=120)),
                ('Branch', models.CharField(max_length=120)),
                ('Semester', models.IntegerField()),
                ('Batch', models.CharField(max_length=120)),
                ('Email', models.EmailField(max_length=254)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.author')),
            ],
        ),
    ]

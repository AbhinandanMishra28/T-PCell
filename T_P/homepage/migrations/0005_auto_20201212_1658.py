# Generated by Django 3.1.4 on 2020-12-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_alumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='adm_staff',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='alumni',
            name='PROFILE_PIC',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='t_p_staff',
            name='Profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

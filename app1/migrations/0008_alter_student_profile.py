# Generated by Django 3.2.2 on 2021-07-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_student_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

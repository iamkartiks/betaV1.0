# Generated by Django 3.2.2 on 2021-07-08 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_student_profile'),
        ('app4', '0017_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.student'),
        ),
    ]

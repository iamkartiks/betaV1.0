# Generated by Django 3.2.2 on 2021-07-07 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_student_profile'),
        ('app4', '0005_auto_20210707_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app4.careeroption')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.student')),
            ],
        ),
    ]
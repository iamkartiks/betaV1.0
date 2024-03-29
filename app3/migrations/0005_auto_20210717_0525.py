# Generated by Django 3.2.2 on 2021-07-17 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_rename_premiumservices_premiumservice'),
        ('app3', '0004_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered',
            name='students',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app3.registeredstudent'),
        ),
        migrations.AlterField(
            model_name='registered',
            name='institute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.institutes'),
        ),
    ]

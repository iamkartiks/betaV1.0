# Generated by Django 3.2.2 on 2021-07-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_studentdemographics'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutes',
            name='sexratio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='StudentDemographics',
        ),
    ]
# Generated by Django 3.2.2 on 2021-07-01 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]

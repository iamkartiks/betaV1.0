# Generated by Django 3.2.2 on 2021-08-18 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_job_job_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]

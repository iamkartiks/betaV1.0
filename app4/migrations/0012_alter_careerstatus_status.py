# Generated by Django 3.2.2 on 2021-07-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0011_alter_careerstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerstatus',
            name='status',
            field=models.CharField(choices=[('NC', 'Not Completed'), ('C', 'Completed')], max_length=100, null=True),
        ),
    ]

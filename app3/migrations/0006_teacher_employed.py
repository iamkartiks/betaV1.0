# Generated by Django 3.2.2 on 2021-07-17 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_rename_premiumservices_premiumservice'),
        ('app3', '0005_auto_20210717_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='employed',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.institutes'),
        ),
    ]
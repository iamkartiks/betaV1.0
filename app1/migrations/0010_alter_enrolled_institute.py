# Generated by Django 3.2.2 on 2021-07-09 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_enrolled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='institute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.institutes'),
        ),
    ]

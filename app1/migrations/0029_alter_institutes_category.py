# Generated by Django 3.2.2 on 2021-08-11 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_auto_20210807_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutes',
            name='category',
            field=models.CharField(choices=[('Playschool', 'Playschool'), ('Highschool', 'Highschool'), ('College', 'College')], max_length=200, null=True),
        ),
    ]
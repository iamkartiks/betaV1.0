# Generated by Django 3.2.2 on 2021-07-13 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_auto_20210713_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.institutes')),
            ],
        ),
    ]
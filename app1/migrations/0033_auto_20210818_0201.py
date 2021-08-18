# Generated by Django 3.2.2 on 2021-08-18 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_eventcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.institutes')),
            ],
        ),
        migrations.DeleteModel(
            name='EventCategories',
        ),
    ]
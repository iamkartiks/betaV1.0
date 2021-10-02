# Generated by Django 3.2.2 on 2021-09-28 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0022_academics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('problem', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(choices=[('Coding', 'Coding'), ('Quiz', 'Quiz'), ('ShortAns', 'ShortAns'), ('LongAns', 'LongAns')], max_length=100, null=True)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard'), ('Very Hard', 'Very Hard')], max_length=100, null=True)),
                ('score', models.IntegerField(null=True)),
                ('level', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app4.level')),
            ],
        ),
    ]
# Generated by Django 3.2.13 on 2023-04-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_num', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('standard', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('phoneno', models.IntegerField()),
            ],
        ),
    ]

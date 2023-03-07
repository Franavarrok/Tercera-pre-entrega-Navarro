# Generated by Django 4.1.7 on 2023-03-07 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('gmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('gmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('grade', models.IntegerField()),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('gmail', models.EmailField(max_length=254)),
            ],
        ),
    ]

# Generated by Django 2.2.24 on 2021-10-31 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bangjobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='chennaijobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hydjobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='punejobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]

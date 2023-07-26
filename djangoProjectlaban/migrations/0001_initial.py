# Generated by Django 4.2.3 on 2023-07-26 04:52

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
                ('fullnames', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('classcode', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=40)),
                ('tscnum', models.CharField(max_length=50)),
            ],
        ),
    ]
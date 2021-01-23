# Generated by Django 2.2.6 on 2019-10-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191012_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='Gender',
            field=models.TextField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
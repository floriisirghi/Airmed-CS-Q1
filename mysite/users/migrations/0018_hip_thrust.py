# Generated by Django 2.2.5 on 2019-10-17 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0017_lunge'),
    ]

    operations = [
        migrations.CreateModel(
            name='hip_thrust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.PositiveIntegerField(blank=True, default=0)),
                ('sets', models.PositiveIntegerField(blank=True, default=0)),
                ('one_rep_max', models.PositiveIntegerField(blank=True, default=0)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

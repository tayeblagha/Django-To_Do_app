# Generated by Django 4.2.20 on 2025-05-22 09:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TODO',
            new_name='TODOO',
        ),
    ]

# Generated by Django 2.2.5 on 2020-01-25 11:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
    ]

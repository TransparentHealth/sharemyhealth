# Generated by Django 2.2.13 on 2020-09-18 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dot_ext', '0021_auto_20200918_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='authflowuuid',
            name='auth_share_demographic_scopes',
            field=models.BooleanField(null=True),
        ),
    ]
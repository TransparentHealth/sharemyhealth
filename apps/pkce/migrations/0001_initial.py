# Generated by Django 2.2.13 on 2021-01-15 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oauth2_provider', '0002_auto_20190406_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeChallenge',
            fields=[
                ('grant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.OAUTH2_PROVIDER_GRANT_MODEL)),
                ('challenge', models.CharField(default=None, max_length=255)),
                ('challenge_method', models.CharField(default='S256', max_length=255)),
            ],
        ),
    ]
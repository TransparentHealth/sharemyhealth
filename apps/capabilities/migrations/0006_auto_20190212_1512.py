# Generated by Django 2.1.2 on 2019-02-12 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capabilities', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protectedcapability',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.Group'),
        ),
    ]

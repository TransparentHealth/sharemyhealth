# Generated by Django 2.1.2 on 2019-02-14 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bluebutton', '0011_auto_20160917_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bluebuttontext',
            name='user',
        ),
        migrations.AlterField(
            model_name='crosswalk',
            name='fhir_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bluebutton.FhirServer'),
        ),
        migrations.DeleteModel(
            name='BlueButtonText',
        ),
    ]

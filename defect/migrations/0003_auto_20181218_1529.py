# Generated by Django 2.0.4 on 2018-12-18 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('defect', '0002_defect'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defect',
            old_name='defectcodecode',
            new_name='defectcode',
        ),
    ]

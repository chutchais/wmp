# Generated by Django 2.0.4 on 2018-12-18 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0004_auto_20181218_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='ndf',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.0.4 on 2018-07-16 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('snippet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('help_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Help Text')),
                ('input_type', models.CharField(choices=[('TEXT', 'Text Box'), ('LIST', 'List Box'), ('RADIO', 'Radio Box'), ('OPTION', 'Option Box'), ('SCRIPT', 'Script Data')], default='TEXT', max_length=10, verbose_name='Input Type')),
                ('default_value', models.CharField(blank=True, max_length=100, null=True, verbose_name='Default Value')),
                ('regexp', models.CharField(blank=True, default='\\w', max_length=100, null=True, verbose_name='RegExp Validation')),
                ('category1', models.CharField(blank=True, max_length=50, null=True)),
                ('category2', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactive')], default='A', max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('expected_return', models.CharField(blank=True, default='TRUE', max_length=100, null=True, verbose_name='Expected Return')),
                ('snippet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='snippet.Snippet', verbose_name='Snippet Code')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('default', models.BooleanField(default=False)),
                ('category1', models.CharField(blank=True, max_length=50, null=True)),
                ('category2', models.CharField(blank=True, max_length=50, null=True)),
                ('ordered', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactive')], default='A', max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='item.Item')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
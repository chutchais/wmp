# Generated by Django 2.0.4 on 2018-07-16 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routing', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('qty', models.IntegerField(default=0)),
                ('regexp', models.CharField(blank=True, default='*', max_length=100, null=True, verbose_name='RegExp Validation')),
                ('category1', models.CharField(blank=True, max_length=50, null=True)),
                ('category2', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactive')], default='A', max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('finished_date', models.DateTimeField(auto_now=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workorders', to='product.Product')),
                ('routing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workorders', to='routing.Routing')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

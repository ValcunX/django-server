# Generated by Django 3.0.5 on 2021-05-01 11:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='py', max_length=4)),
                ('image_id', models.CharField(default='codercom/code-server', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(6)])),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('volume_id', models.CharField(max_length=100)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='backend.Language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.User')),
            ],
        ),
    ]

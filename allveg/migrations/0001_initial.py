# Generated by Django 5.0.2 on 2024-10-13 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, choices=[('Farmer', 'Farmer'), ('AgriMember', 'AgriMember'), ('Leader', 'Leader'), ('Manager', 'Manager'), ('GeneralManager', 'GeneralManager')], default='Farmer', max_length=20, null=True)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='allveg.user')),
            ],
        ),
    ]

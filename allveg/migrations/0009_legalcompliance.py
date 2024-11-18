# Generated by Django 5.0.2 on 2024-10-13 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allveg', '0008_rename_mobile_number_generalmanagers_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalCompliance',
            fields=[
                ('compliance_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(blank=True, choices=[('AgriMember', 'AgriMember'), ('Farmer', 'Farmer'), ('GeneralManager', 'GeneralManager'), ('Leader', 'Leader'), ('Manager', 'Manager')], max_length=20, null=True)),
                ('fpo_details', models.CharField(blank=True, max_length=255, null=True)),
                ('fpo_membership', models.BooleanField(blank=True, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=50, null=True)),
                ('kcc_number', models.CharField(blank=True, max_length=55, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=55, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='allveg.users')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-10-17 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allveg', '0018_generalmanagers_bank_details_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='created_by',
            new_name='modified_by',
        ),
    ]

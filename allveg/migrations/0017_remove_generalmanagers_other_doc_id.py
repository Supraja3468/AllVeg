# Generated by Django 5.0.2 on 2024-10-16 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allveg', '0016_rename_created_by_legalcompliance_modified_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalmanagers',
            name='other_doc_id',
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allveg', '0036_alter_buyer_buyer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='document_type',
            field=models.CharField(choices=[('Identity', 'Identity'), ('Address', 'Address'), ('Bank', 'Bank'), ('Land', 'Land'), ('Photo', 'Photo'), ('Education', 'Education'), ('Other', 'Other'), ('Business', 'Business'), ('GST', 'GST'), ('PanCard', 'PanCard'), ('Vehicle_RC_Book', 'Vehicle_RC_Book'), ('Vehicle_Insurance', 'Vehicle_Insurance'), ('Driving_License', 'Driving_License'), ('Bank_Details', 'Bank_Details')], max_length=20),
        ),
    ]

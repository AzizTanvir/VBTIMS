# Generated by Django 5.0.2 on 2024-10-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0005_alter_incident_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

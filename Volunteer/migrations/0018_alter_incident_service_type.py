# Generated by Django 5.0.2 on 2024-11-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0017_alter_incident_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='service_type',
            field=models.CharField(choices=[('fire', 'Fire'), ('police', 'Police'), ('ambulance', 'Ambulance')], default='nothing', max_length=50),
        ),
    ]

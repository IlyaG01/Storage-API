# Generated by Django 4.1.3 on 2022-12-07 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("storage_sensors", "0002_alter_sensors_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sensors",
            old_name="name_sensor",
            new_name="sensor_name",
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storage_sensors", "0009_rename_machines_type_sensors_machine"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prediction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type_alert", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=20)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
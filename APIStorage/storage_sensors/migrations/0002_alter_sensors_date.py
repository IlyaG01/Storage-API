# Generated by Django 4.1.3 on 2022-12-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storage_sensors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sensors",
            name="date",
            field=models.CharField(max_length=10),
        ),
    ]
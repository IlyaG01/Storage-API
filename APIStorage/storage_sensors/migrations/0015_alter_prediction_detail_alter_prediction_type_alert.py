# Generated by Django 4.1.3 on 2022-12-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storage_sensors", "0014_alter_prediction_type_alert"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prediction",
            name="detail",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="type_alert",
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-16 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("storage_sensors", "0006_rename_second_name_employee_last_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Machines",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Positions",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Schedule",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="user_id",
            new_name="telegram_id",
        ),
        migrations.AddField(
            model_name="employee",
            name="vacation",
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Area_of_Responsibility",
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
                (
                    "employee_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="storage_sensors.employee",
                    ),
                ),
                (
                    "machine_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="storage_sensors.machines",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="employee",
            name="position",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="storage_sensors.positions",
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="work_schedule",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="storage_sensors.schedule",
            ),
        ),
        migrations.AddField(
            model_name="sensors",
            name="machines_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="storage_sensors.machines",
            ),
        ),
    ]

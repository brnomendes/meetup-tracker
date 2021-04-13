# Generated by Django 3.2 on 2021-04-13 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0002_groupurlname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groupurlname",
            name="urlname",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="location",
            name="city",
            field=models.CharField(max_length=256),
        ),
        migrations.CreateModel(
            name="MeetupGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField(blank=True)),
                ("status", models.CharField(blank=True, max_length=256)),
                ("link", models.CharField(blank=True, max_length=1024)),
                ("photo_link", models.CharField(blank=True, max_length=1024)),
                ("member_count", models.IntegerField(blank=True, null=True)),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tracker.location"
                    ),
                ),
                (
                    "urlname",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="tracker.groupurlname"
                    ),
                ),
            ],
        ),
    ]
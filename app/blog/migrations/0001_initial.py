# Generated by Django 3.2 on 2021-05-09 13:21

import martor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=200, null=True)),
                ("slug", models.SlugField(editable=False, unique=True)),
                ("content", martor.models.MartorField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("meta_description", models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="HomePageContent",
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
                ("content", martor.models.MartorField(null=True)),
            ],
        ),
    ]

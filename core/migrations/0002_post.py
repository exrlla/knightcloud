# Generated by Django 4.2 on 2023-05-04 23:13

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("user", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="post_images")),
                ("caption", models.TextField(blank=True)),
                ("link", models.CharField(max_length=300)),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
                ("no_of_likes", models.IntegerField(default=0)),
            ],
        ),
    ]

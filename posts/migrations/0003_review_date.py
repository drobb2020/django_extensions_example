# Generated by Django 5.0.4 on 2024-05-04 22:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_review_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

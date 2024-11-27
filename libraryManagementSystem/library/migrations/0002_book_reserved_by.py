# Generated by Django 5.1 on 2024-11-27 18:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="reserved_by",
            field=models.ManyToManyField(
                blank=True, related_name="reserved_books", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]

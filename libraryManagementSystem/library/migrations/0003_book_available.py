# Generated by Django 5.1 on 2024-11-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_book_reserved_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="available",
            field=models.BooleanField(default=True),
        ),
    ]

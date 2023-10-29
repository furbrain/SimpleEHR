# Generated by Django 4.2.6 on 2023-10-27 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("EHR", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="code",
            name="term_code",
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="code",
            name="text",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-19 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("executor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="executorprofile",
            name="phone",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

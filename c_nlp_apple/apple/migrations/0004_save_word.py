# Generated by Django 4.1 on 2023-07-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apple", "0003_european_standard_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="Save_Word",
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
                    "word",
                    models.CharField(
                        default="", max_length=250, null=True, verbose_name="单词"
                    ),
                ),
                ("create_date", models.DateField(auto_now=True, verbose_name="创建日期")),
            ],
        ),
    ]

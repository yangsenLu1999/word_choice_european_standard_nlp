# Generated by Django 4.1 on 2023-07-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apple", "0007_alter_words_bank_pos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="words_bank",
            name="inflection",
            field=models.TextField(default="", null=True, verbose_name="变形式"),
        ),
    ]

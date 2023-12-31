# Generated by Django 4.1 on 2023-07-13 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Adjective",
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
                ("word", models.CharField(max_length=50)),
                ("pos", models.CharField(max_length=50)),
                (
                    "comparative",
                    models.CharField(default="", max_length=150, null=True),
                ),
                (
                    "superlative",
                    models.CharField(default="", max_length=150, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Adverb",
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
                ("word", models.CharField(max_length=50)),
                ("pos", models.CharField(max_length=50)),
                (
                    "comparative",
                    models.CharField(default="", max_length=150, null=True),
                ),
                (
                    "superlative",
                    models.CharField(default="", max_length=150, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Adverbial_fixation",
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
                ("word", models.CharField(max_length=150)),
                ("meaning", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Categorydict",
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
                ("word", models.CharField(max_length=150)),
                ("pos", models.CharField(max_length=50)),
                ("type", models.CharField(max_length=50)),
                ("words", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="fixedMatch",
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
                ("text", models.CharField(max_length=150)),
                ("vbd", models.CharField(max_length=50)),
                ("vbg", models.CharField(max_length=50)),
                ("vbn", models.CharField(max_length=50)),
                ("vbz", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Moun",
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
                ("words", models.CharField(max_length=50)),
                ("word", models.CharField(max_length=50)),
                ("pos", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Nonverbpos",
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
                ("word", models.CharField(max_length=50)),
                ("pos", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Ordinal_Numeral",
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
                ("cardinal", models.CharField(max_length=150)),
                ("ordinal", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Prep",
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
                ("word", models.CharField(max_length=50)),
                ("pos", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Pronoun",
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
                ("word", models.CharField(max_length=50)),
                ("pos", models.CharField(max_length=50)),
                ("type", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Quantifierlemma",
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
                ("word", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Verbpluspos",
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
                ("word", models.CharField(max_length=50)),
                ("pos", models.CharField(max_length=50)),
                ("_pos", models.CharField(max_length=50)),
                ("vbz", models.CharField(max_length=50)),
                ("vbg", models.CharField(max_length=50)),
                ("vbd", models.CharField(max_length=50)),
                ("vbn", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Verbpluspos_Double",
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
                ("word", models.CharField(max_length=50)),
                ("pos", models.CharField(max_length=50)),
                ("_pos", models.CharField(max_length=50)),
                ("vbz", models.CharField(max_length=50)),
                ("vbg", models.CharField(max_length=50)),
                ("vbd", models.CharField(max_length=50)),
                ("vbn", models.CharField(max_length=50)),
            ],
        ),
    ]

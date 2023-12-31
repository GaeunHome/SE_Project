# Generated by Django 4.1 on 2023-06-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finalapp", "0002_auto_20230604_1634"),
    ]

    operations = [
        migrations.CreateModel(
            name="MassageChair",
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
                ("MID", models.CharField(max_length=20)),
                ("MState", models.CharField(max_length=50)),
                ("PID", models.CharField(max_length=20)),
                ("BID", models.CharField(max_length=20)),
                ("MPrice", models.DecimalField(decimal_places=2, max_digits=10)),
                ("MCost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("MAmount", models.IntegerField()),
                ("MClass", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="purchase",
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
                ("PID", models.CharField(max_length=20)),
                ("BID", models.CharField(max_length=20)),
                ("MID", models.CharField(max_length=20)),
                ("PCost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("PAmount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="SalesDetail",
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
                ("BID", models.CharField(max_length=20)),
                ("SID", models.CharField(max_length=20)),
                ("CID", models.CharField(max_length=20)),
                ("MID", models.CharField(max_length=20)),
                ("SAmount", models.IntegerField()),
                ("SPrice", models.DecimalField(decimal_places=2, max_digits=10)),
                ("SDiscount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("SPay", models.DecimalField(decimal_places=2, max_digits=10)),
                ("SDate", models.DateField()),
                ("SRepurchase", models.BooleanField()),
                ("SPayment", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="customer",
            name="CActrecord",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="CDemand_description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="CSpecial_requests",
            field=models.TextField(blank=True),
        ),
    ]

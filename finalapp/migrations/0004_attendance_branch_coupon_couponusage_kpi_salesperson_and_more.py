# Generated by Django 4.1 on 2023-06-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finalapp", "0003_massagechair_purchase_salesdetail_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                ("SID", models.CharField(max_length=20)),
                ("date", models.DateField()),
                ("SW", models.TimeField()),
                ("SG", models.TimeField()),
                ("SL", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Branch",
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
                ("SAc", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Coupon",
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
                ("AID", models.CharField(max_length=20)),
                ("AName", models.CharField(max_length=100)),
                ("AContent", models.TextField()),
                ("AUse", models.BooleanField()),
                ("ADeadline", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="CouponUsage",
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
                ("AID", models.CharField(max_length=20)),
                ("CID", models.CharField(max_length=20)),
                ("AUsedate", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="KPI",
            fields=[
                (
                    "KID",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("KName", models.CharField(max_length=100)),
                ("KSet", models.CharField(max_length=50)),
                ("KReach", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Salesperson",
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
                ("SID", models.CharField(max_length=20)),
                ("SQ", models.IntegerField()),
                ("SR", models.DecimalField(decimal_places=2, max_digits=10)),
                ("STQ", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="SalesTarget",
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
                ("TID", models.CharField(max_length=20)),
                ("BID", models.CharField(max_length=20)),
                ("SID", models.CharField(max_length=20)),
                ("TSet", models.CharField(max_length=50)),
                ("TReach", models.CharField(max_length=50)),
                ("TSetdate", models.DateField()),
                ("TDeadline", models.DateField()),
            ],
        ),
    ]
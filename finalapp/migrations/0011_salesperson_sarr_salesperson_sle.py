# Generated by Django 4.1 on 2023-06-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finalapp", "0010_salesperson_sm1_salesperson_sm2_salesperson_sm3"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesperson", name="SARR", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="salesperson", name="SLE", field=models.IntegerField(null=True),
        ),
    ]

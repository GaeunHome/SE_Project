# Generated by Django 4.1 on 2023-06-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finalapp", "0008_branch_bname_salesperson_sname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salesperson", name="SR", field=models.IntegerField(),
        ),
    ]

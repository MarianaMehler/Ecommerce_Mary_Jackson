# Generated by Django 5.0.3 on 2024-03-31 21:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_MJ", "0003_rename_clientes_cliente"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="nome_produto",
            field=models.CharField(default="", max_length=200),
        ),
    ]

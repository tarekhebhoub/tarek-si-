# Generated by Django 4.1.4 on 2023-01-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_acheter_produit_facture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acheter_produit',
            name='montant_HT',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='acheter_produit',
            name='unité_HT',
            field=models.FloatField(),
        ),
    ]

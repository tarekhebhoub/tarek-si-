# Generated by Django 4.1.4 on 2023-01-21 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_stock_prix_vente_stock_unité_ht'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sortie_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Entree_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.produit')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-12 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.PositiveIntegerField()),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.produit')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-04 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_fournisseur_facture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fournisseur',
            name='facture',
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='facture',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='fourner_de_factuers', to='app1.facture'),
            preserve_default=False,
        ),
    ]
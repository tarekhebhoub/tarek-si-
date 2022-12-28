from django.db import models

# Create your models here.
class Produit(models.Model):
    code=models.IntegerField(primary_key=True)
    designation=models.CharField(max_length=50)
    type=models.ForeignKey('Type_Produit',related_name='Type',on_delete=models.CASCADE)
    def __str__(self):
        return self.designation

class Type_Produit(models.Model):
    code=models.IntegerField(primary_key=True)
    designation=models.CharField(max_length=50)
    def __str__(self):
        return self.designation

class Client(models.Model):
    code=models.IntegerField(primary_key=True)
    nom_prenom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    téléphone=models.IntegerField()

class Fournisseur(models.Model):
    code=models.IntegerField(primary_key=True)
    nom_prenom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    téléphone=models.IntegerField()
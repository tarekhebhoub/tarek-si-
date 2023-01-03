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
    def __str__(self):
        return self.nom_prenom

class Fournisseur(models.Model):
    code=models.IntegerField(primary_key=True)
    nom_prenom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    téléphone=models.IntegerField()
    def __str__(self):
        return self.nom_prenom

class Commande_un_Produit(models.Model):
    produit=models.ForeignKey(Produit,related_name='quantity_produit',on_delete=models.CASCADE)
    # commande=models.ForeignKey('Commande_Produits',related_name='commande_produit',on_delete=models.CASCADE)
    qte=models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.produit.designation)+', '+str(self.qte)

class Commande_Produits(models.Model):
    produit_commander=models.ManyToManyField(Commande_un_Produit,related_name="list_des_commande")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # def __str__(self):
        # return self.quantites.__str__()*


class Facture(models.Model):
    Num_Doc=models.IntegerField(primary_key=True)
    date=models.DateField()
    fournisseur=models.ForeignKey(Fournisseur,related_name='fournisseur',on_delete=models.CASCADE)
    produit_achat=models.ManyToManyField('Acheter_Produit',related_name="des_produits_acheter")

class Acheter_Produit(models.Model):
    produit=models.ForeignKey(Produit,related_name='achete_produit',on_delete=models.CASCADE)
    qte=models.PositiveIntegerField()
    unité_HT=models.FloatField()
    def __str__(self):
        return str(self.produit)+', '+str(self.qte)

class BL(models.Model):
    TVA=models.PositiveIntegerField(default=19)
    remise=models.PositiveIntegerField()
    def __str__(self):
        return str(self.TVA)+' , '+str(self.remise)
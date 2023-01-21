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
    # facture=models.ForeignKey('Facture',related_name='fourner_de_factuers',on_delete=models.CASCADE,null=True,blank=True)

    # facture=models.ManyToManyField('Facture',related_name='fourner_de_factuers',blank=True)
    def __str__(self):
        return self.nom_prenom

class Commande_un_Produit(models.Model):
    produit=models.ForeignKey(Produit,related_name='quantity_produit',on_delete=models.CASCADE)
    # commande=models.ForeignKey('Commande_Produits',related_name='commande_produit',on_delete=models.CASCADE)
    qte=models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.produit.designation)+', '+str(self.qte)

class Bon_Cammande(models.Model):
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
    def __str__(self):
        return 'fournisseur de cette facture: '+str(self.fournisseur)[0:10]


class Acheter_Produit(models.Model):
    produit=models.ForeignKey(Produit,related_name='achete_produit',on_delete=models.CASCADE)
    qte=models.PositiveIntegerField()
    unité_HT=models.FloatField()
    prix_vente=models.FloatField()
    def __str__(self):
        return str(self.produit)+', '+str(self.qte)

class BL(models.Model):
    facture=models.ForeignKey(Facture,related_name="Bl_facture",on_delete=models.CASCADE)
    TVA=models.PositiveIntegerField(default=19)
    remise=models.PositiveIntegerField()
    def __str__(self):
        return str(self.TVA)+' , '+str(self.remise)

class Vente(models.Model):
    client=models.ForeignKey(Client,related_name="client_vente",on_delete=models.CASCADE)
    list_produits=models.ManyToManyField('Vente_Produit',related_name="des_produit_vente")
    def __str__(self):
        return 'vente à: '+self.client.nom_prenom

class Vente_Produit(models.Model):
    produit=models.ForeignKey(Produit,related_name='vente_un_produit',on_delete=models.CASCADE)
    qte=models.PositiveIntegerField()
    def __str__(self):
        return str(self.produit)+', '+str(self.qte)

class Credit(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    payement=models.FloatField()
    def __str__(self):
        return 'payment client: '+str(self.client)





class Stock(models.Model):
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    qte=models.PositiveIntegerField()
    unité_HT=models.FloatField()
    prix_vente=models.FloatField()
    def __str__(self):
        return str(self.produit)

class Entree_Stock(models.Model):
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    qte=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Entree: '+str(self.produit)+' '+str(self.qte)

class Sortie_Stock(models.Model):
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    qte=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Sortie: '+str(self.produit)+' '+str(self.qte)
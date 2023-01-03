from rest_framework import serializers
from .models import Type_Produit,Facture,Fournisseur,Produit,Client,Commande_un_Produit,Commande_Produits,Acheter_Produit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produit
        fields='__all__'

class Type_ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type_Produit
        fields='__all__'
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'

class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fournisseur
        fields='__all__'

class Commande_Produits_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Commande_Produits
        fields='__all__'

class Commande_un_Produit_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Commande_un_Produit
        fields='__all__'
    
class Achet_un_Produit_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Acheter_Produit
        # fields=['produit','qte','unité_HT']
        fields='__all__'

class Facture_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Facture
        # fields=['produit','qte','unité_HT']
        fields='__all__'
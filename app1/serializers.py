from rest_framework import serializers
from .models import Type_Produit,Sortie_Stock,Entree_Stock,Stock,Vente_Produit,Vente,Facture,BL,Fournisseur,Produit,Client,Commande_un_Produit,Bon_Cammande,Acheter_Produit

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
        model=Bon_Cammande
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
class BL_Serializer(serializers.ModelSerializer):
    class Meta:
        model=BL
        fields='__all__'

class Vente_Produit_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Vente_Produit
        fields='__all__'

class Vente_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Vente
        fields='__all__'

class Stock_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields='__all__'

class Entree_Stock_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Entree_Stock
        fields='__all__'

class Sortie_Stock_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Sortie_Stock
        fields='__all__'
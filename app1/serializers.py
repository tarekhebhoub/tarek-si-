from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import Type_Produit,Fournisseur,Produit,Client

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


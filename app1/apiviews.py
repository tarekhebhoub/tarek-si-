from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Type_Produit,Fournisseur,Produit,Client
from .serializers import ProduitSerializer,Type_ProduitSerializer,ClientSerializer,FournisseurSerializer

class ListProduits(APIView):
    serializer_class=ProduitSerializer

    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

    def post(self,request):
        data=request.data
        print(data)
        serializer=ProduitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class GetProduit(APIView):
    def get(self,request,pk):
        produit=Produit.objects.get(code=pk)
        serializer=ProduitSerializer(produit)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        produit = Produit.objects.get(code=pk)
        produit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Type_Produit,Fournisseur,Produit,Client
from .serializers import ProduitSerializer,Type_ProduitSerializer,ClientSerializer,FournisseurSerializer
from django.http import FileResponse
import pdfkit

class ListProduits(APIView):
    serializer_class=ProduitSerializer
    def get(self,request):
        query=request.GET.get('recherche')
        if(query):
            produits=Produit.objects.filter(designation__contains=query)
            serialize=ProduitSerializer(produits,many=True)
            return Response(serialize.data)
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
    def post(self,request):
        data=request.data
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
    def put(self,request,pk):
        data=request.data
        produit=Produit.objects.get(code=pk)
        produit.designation=data.get('designation')
        produit.type=data.get('type')
        produit.save()
        serializer=ProduitSerializer(produit)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Imprimer_Produit(APIView):

    def generate_html_file(self):
        strTable = "<html><head><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65' crossorigin='anonymous'></head><body><table class='table'><thead class='table-dark'><tr><th scope='col'>Code</th><th scope='col'>Desegnation</th><th scope='col'>Type</th></tr></thead><tbody>"
        produits=Produit.objects.all()
        for prd in produits: 
            strRW = "<tr><td>"+str(prd.code)+ "</td><td>"+prd.designation+"</td><td>"+str(prd.type)+"</td></tr>"
            strTable = strTable+strRW
        
        strTable = strTable+"</tbody></table></body></html>"   
        hs = open("pdf.html", 'w')
        hs.write(strTable)

    def get(self,request):
        
        self.generate_html_file()
        pdfkit.from_file('pdf.html', 'produits.pdf')
        pdf=open('produits.pdf','rb')
        
        return FileResponse(pdf,as_attachment=True, content_type='application/pdf')



class ListType(APIView):
    serializer_class=Type_ProduitSerializer
    def get(self,request):
        query=request.GET.get('recherche')
        if(query):
            types=Type_Produit.objects.filter(designation__contains=query)
            serialize=Type_ProduitSerializer(types,many=True)
            return Response(serialize.data)
        types = Type_Produit.objects.all()
        serializer = Type_ProduitSerializer(types, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=Type_ProduitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
class GetType(APIView):
    def get(self,request,pk):
        type=Type_Produit.objects.get(code=pk)
        serializer=Type_ProduitSerializer(type)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        type = Type_Produit.objects.get(code=pk)
        type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        data=request.data
        type=Type_Produit.objects.get(code=pk)
        type.designation=data.get('designation')
        type.save()
        serializer=Type_ProduitSerializer(type)
        return Response(serializer.data,status=status.HTTP_200_OK)
        # else:
            # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Imprimer_Types(APIView):
    def generate_html_file(self):
        strTable = "<html><head><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65' crossorigin='anonymous'></head><body><table class='table'><thead class='table-dark'><tr><th scope='col'>Code</th><th scope='col'>Desegnation</th></tr></thead><tbody>"
        types=Type_Produit.objects.all()
        for type in types: 
            strRW = "<tr><td>"+str(type.code)+ "</td><td>"+type.designation+"</td></tr>"
            strTable = strTable+strRW
        
        strTable = strTable+"</tbody></table></body></html>"   
        hs = open("pdf.html", 'w')
        hs.write(strTable)

    def get(self,request):
        self.generate_html_file()
        pdfkit.from_file('pdf.html', 'type_de_produits.pdf')
        pdf=open('type_de_produits.pdf','rb')
        return FileResponse(pdf)


class ListClient(APIView):
    serializer_class=ClientSerializer
    def get(self,request):
        query=request.GET.get('recherche')
        if(query):
            clients=Client.objects.filter(nom_prenom__contains=query)
            serialize=ClientSerializer(clients,many=True)
            return Response(serialize.data)
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
class GetClient(APIView):
    def get(self,request,pk):
        client=Client.objects.get(code=pk)
        serializer=ClientSerializer(client)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        client = Client.objects.get(code=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        client=Client.objects.get(code=pk)
        serializer=ClientSerializer(client,data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Imprimer_Clients(APIView):
    def generate_html_file(self):
        strTable = "<html><head><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65' crossorigin='anonymous'></head><body><table class='table'><thead class='table-dark'><tr><th scope='col'>Code</th><th scope='col'>Nom & Prenom</th><th>Adresse</th><th>Telephone</th></tr></thead><tbody>"
        client=Client.objects.all()
        for client in client: 
            strRW = "<tr><td>"+str(client.code)+ "</td><td>"+client.nom_prenom+"</td><td>"+client.adresse+"</td><td>"+str(client.téléphone)+"</td></tr>"
            strTable = strTable+strRW
        
        strTable = strTable+"</tbody></table></body></html>"   
        hs = open("pdf.html", 'w')
        hs.write(strTable)

    def get(self,request):
        self.generate_html_file()
        pdfkit.from_file('pdf.html', 'Clients.pdf')
        pdf=open('Clients.pdf','rb')
        return FileResponse(pdf)


class ListFournisseur(APIView):
    serializer_class=FournisseurSerializer
    def get(self,request):
        query=request.GET.get('recherche')
        if(query):
            fournisseur=Fournisseur.objects.filter(nom_prenom__contains=query)
            serialize=FournisseurSerializer(fournisseur,many=True)
            return Response(serialize.data)
        fournisseur = Fournisseur.objects.all()
        serializer = FournisseurSerializer(fournisseur, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=FournisseurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
class GetFournisseur(APIView):
    def get(self,request,pk):
        fournisseur=Fournisseur.objects.get(code=pk)
        serializer=FournisseurSerializer(fournisseur)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        fournisseur = Fournisseur.objects.get(code=pk)
        fournisseur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        fournisseur=Fournisseur.objects.get(code=pk)
        serializer=ClientSerializer(fournisseur,data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Imprimer_Fournisseurs(APIView):
    def generate_html_file(self):
        strTable = "<html><head><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65' crossorigin='anonymous'></head><body><table class='table'><thead class='table-dark'><tr><th scope='col'>Code</th><th scope='col'>Nom & Prenom</th><th>Adresse</th><th>Telephone</th></tr></thead><tbody>"
        fournisseurs=Fournisseur.objects.all()
        for fournisseur in fournisseurs: 
            strRW = "<tr><td>"+str(fournisseur.code)+ "</td><td>"+fournisseur.nom_prenom+"</td><td>"+fournisseur.adresse+"</td><td>"+str(fournisseur.téléphone)+"</td></tr>"
            strTable = strTable+strRW
        
        strTable = strTable+"</tbody></table></body></html>"   
        hs = open("pdf.html", 'w')
        hs.write(strTable)

    def get(self,request):
        self.generate_html_file()
        pdfkit.from_file('pdf.html', 'Fournisseurs.pdf')
        pdf=open('Fournisseurs.pdf','rb')
        return FileResponse(pdf)
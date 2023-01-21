from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Type_Produit,BL,Facture,Sortie_Stock,Entree_Stock,Vente,Stock,Vente_Produit,Acheter_Produit,Fournisseur,Produit,Client,Bon_Cammande,Commande_un_Produit
from .serializers import ProduitSerializer,Entree_Stock_Serializer,Sortie_Stock_Serializer,Stock_Serializer,Vente_Produit_Serializer,Vente_Serializer,BL_Serializer,Facture_Serializer,Achet_un_Produit_Serializer,Type_ProduitSerializer,Commande_un_Produit_Serializer,ClientSerializer,Commande_Produits_Serializer,FournisseurSerializer
from django.http import FileResponse
import pdfkit
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

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
        data=JSONParser().parse(request.data)
        serializer=ProduitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)

class GetProduit(APIView):
    def get(self,request,pk):
        produit=Produit.objects.get(code=pk)
        serializer=ProduitSerializer(produit)
        return JsonResponse(serializer.data,safe=False)
    
    def delete(self, request, pk):
        produit = Produit.objects.get(code=pk)
        produit.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT,safe=False)
    def put(self,request,pk):
        data=JSONParser().parse(request.data)
        produit=Produit.objects.get(code=pk)
        produit.designation=data.get('designation')
        produit.type=data.get('type')
        produit.save()
        serializer=ProduitSerializer(produit)
        return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
        

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
        
        return FileResponse(pdf)



class ListType(APIView):
    serializer_class=Type_ProduitSerializer
    def get(self,request):
        query=request.GET.get('recherche')
        if(query):
            types=Type_Produit.objects.filter(designation__contains=query)
            serialize=Type_ProduitSerializer(types,many=True)
            return JsonResponse(serialize.data,safe=False)
        types = Type_Produit.objects.all()
        serializer = Type_ProduitSerializer(types, many=True)
        return JsonResponse(serializer.data,safe=False)
    
    def post(self,request):
        data=JSONParser.parse(request.data)
        serializer=Type_ProduitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)


        
class GetType(APIView):
    serializer_class=Type_ProduitSerializer
    def get(self,request,pk):
        type=Type_Produit.objects.get(code=pk)
        serializer=Type_ProduitSerializer(type)
        return JsonResponse(serializer.data,safe=False)
    
    def delete(self, request, pk):
        type = Type_Produit.objects.get(code=pk)
        type.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT,safe=False)
    def put(self,request,pk):
        data=JSONParser().parse(request.data)
        type=Type_Produit.objects.get(code=pk)
        type.designation=data.get('designation')
        type.save()
        serializer=Type_ProduitSerializer(type)
        return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
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
        return JsonResponse(serializer.data,safe=False)
    
    def post(self,request):
        data=JSONParser().parse(request)
        print(data)
        serializer=ClientSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)


        
class GetClient(APIView):
    def get(self,request,pk):
        client=Client.objects.get(code=pk)
        serializer=ClientSerializer(client)
        return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
    
    def delete(self, request, pk):
        client = Client.objects.get(code=pk)
        client.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT,safe=False)
        # return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        client=Client.objects.get(code=pk)
        data=JSONParser().parse(request)
        serializer=ClientSerializer(client,data=data)
        if serializer.is_valid():   
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
            # return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)

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
        data=JSONParser().parse(request)
        serializer=FournisseurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)


        
class GetFournisseur(APIView):
    def get(self,request,pk):
        fournisseur=Fournisseur.objects.get(code=pk)
        serializer=FournisseurSerializer(fournisseur)
        return JsonResponse(serializer.data,safe=False)
    
    def delete(self, request, pk):
        fournisseur = Fournisseur.objects.get(code=pk)
        fournisseur.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT,safe=False)
    def put(self,request,pk):
        fournisseur=Fournisseur.objects.get(code=pk)
        data=JSONParser().parse(request)
        serializer=FournisseurSerializer(fournisseur,data=data)
        if serializer.is_valid():   
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)

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






class Commander_Produits(APIView):
    serializer_class=Commande_Produits_Serializer
    def get(self,request):
        commandes=Bon_Cammande.objects.all()
        serializer=Commande_Produits_Serializer(commandes,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=JSONParser().parse(request)
        serializer=Commande_Produits_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)

class Get_Commander_Produits(APIView):
    serializer_class=Commande_Produits_Serializer
    def get(self,request,pk):
        Commande=Bon_Cammande.objects.get(id=pk)
        serializer=Commande_Produits_Serializer(Commande)
        return JsonResponse(serializer.data,safe=False)
    
    def delete(self, request, pk):
        Commande = Bon_Cammande.objects.get(id=pk)
        Commande.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT,safe=False)
    def put(self,request,pk):
        Commande=Bon_Cammande.objects.get(id=pk)
        data=JSONParser().parse(request)
        serializer=Commande_Produits_Serializer(Commande,data=data)
        if serializer.is_valid():   
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)

# IMprimer lA commande

class Imprimer_Bon_Commande(APIView):
    def generate_html_file(self,pk):
        commande=Bon_Cammande.objects.get(id=pk)
        strTable = "<html><head><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65' crossorigin='anonymous'></head><body><div><h1>ID de Commande: "+str(commande.id)+"</h1> <br> <h3>"+"Created at: "+str(commande.created_at)+"</h3><br><h3>"+"Updated at: "+str(commande.updated_at)+"</h3></div><table class='table'><thead class='table-dark'><tr><th scope='col'>Designation</th><th scope='col'>Quntity</th></tr></thead><tbody>"
        produits_commander=Bon_Cammande.produit_commander.through.objects.filter(bon_cammande_id=pk) 
        produit_commander=produits_commander.values('commande_un_produit_id')

        # print(produits.values('commande_un_produit_id').commande_un_produit_id)
        for prd in produit_commander:
            produit=Commande_un_Produit.objects.get(id=prd['commande_un_produit_id'])
            strRW = "<tr><td>"+str(produit.produit)+ "</td><td>"+str(produit.qte)+"</td></tr>"
            strTable = strTable+strRW
        
        strTable = strTable+"</tbody></table></body></html>"   
        hs = open("pdf.html", 'w')
        hs.write(strTable)

    def get(self,request,pk):
        self.generate_html_file(pk)
        pdfkit.from_file('pdf.html', 'Bon_Commande.pdf')
        pdf=open('Bon_Commande.pdf','rb')
        return FileResponse(pdf)





class Commander_un_Produit(APIView):
    serializer_class=Commande_un_Produit_Serializer
    def get(self,request):
        quntitys=Commande_un_Produit.objects.all()
        serializer=Commande_un_Produit_Serializer(quntitys,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=JSONParser().parse(request)
        serializer=Commande_un_Produit_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)

class Get_Commander_un_Produit(APIView):
    serializer_class=Commande_un_Produit_Serializer
    def get(self,request,pk):
        Commande=Commande_un_Produit.objects.get(id=pk)
        serializer=Commande_un_Produit_Serializer(Commande)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        Commande = Commande_un_Produit.objects.get(id=pk)
        Commande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        Commande=Commande_un_Produit.objects.get(id=pk)
        data=JSONParser().parse(request)
        serializer=Commande_un_Produit_Serializer(Commande,data=data)
        if serializer.is_valid():   
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)
        


# section Achat Facture
class Acheter_un_Produit(APIView):
    serializer_class=Achet_un_Produit_Serializer
    def get(self,request):
        produit_achete=Acheter_Produit.objects.all()
        serializer=Achet_un_Produit_Serializer(produit_achete,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=JSONParser().parse(request)
        serializer=Achet_un_Produit_Serializer(data=data)
        if serializer.is_valid():
            # serializer.validated_data['montant_HT']=serializer.validated_data['unité_HT']*serializer.validated_data['qte']
            serializer.save()
            produit_stock=Stock.objects.filter(produit=data['produit'])
            print(produit_stock)
            # insert the new produit in the Stock

            if produit_stock:
                for produit in produit_stock:
                    if(produit.unité_HT==serializer.validated_data['unité_HT'] and produit.prix_vente==serializer.validated_data['prix_vente']):
                        produit.qte+=int(serializer.validated_data['qte'])
                        produit.save()
                        return Response(serializer.data,status=status.HTTP_201_CREATED)
            
            serializer1=Stock_Serializer(data=data)
            if serializer1.is_valid():
                serializer1.save()
            # Acheter_Produit.montant_ht(self)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Get_Acheter_un_Produit(APIView):
    serializer_class=Achet_un_Produit_Serializer
    def get(self,request,pk):
        produit_achete=Acheter_Produit.objects.get(id=pk)
        serializer=Achet_un_Produit_Serializer(produit_achete)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        produit_achete = Acheter_Produit.objects.get(id=pk)
        produit_achete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        produit_achete=Acheter_Produit.objects.get(id=pk)
        data=JSONParser().parse(request)
        serializer=Achet_un_Produit_Serializer(produit_achete,data=data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

# Facture
class Factures(APIView):
    serializer_class=Facture_Serializer
    def get(self,request):
        factures=Facture.objects.all()
        serializer=Facture_Serializer(factures,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=JsonResponse().parse(request)
        serializer=Facture_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Get_Facture(APIView):
    serializer_class=Facture_Serializer
    def get(self,request,pk):
        facture=Facture.objects.get(id=pk)
        serializer=Facture_Serializer(Facture)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        facture = Facture.objects.get(id=pk)
        facture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        facture=Facture.objects.get(id=pk)
        data=JsonResponse().parse(request)
        serializer=Facture_Serializer(facture,data=data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class Imprimer_Facture(APIView):
    def generate_html_file(self,pk):
        facture=Facture.objects.get(id=pk)
        strTable = "<html><head><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65' crossorigin='anonymous'></head><body><div><h1>Num de Document: "+str(facture.Num_Doc)+"</h1> <br> <h3>"+"Date: "+str(facture.date)+"</h3><br><h3>"+"Fournisseur: "+str(facture.fournisseur)+"</h3></div><table class='table'><thead class='table-dark'><tr><th scope='col'>Designation</th><th scope='col'>Quntity</th></tr></thead><tbody>"
        produits_commander=Bon_Cammande.produit_commander.through.objects.filter(commande_produits_id=pk) 
        produit_commander=produits_commander.values('commande_un_produit_id')

        # print(produits.values('commande_un_produit_id').commande_un_produit_id)
        for prd in produit_commander:
            produit=Commande_un_Produit.objects.get(id=prd['commande_un_produit_id'])
            strRW = "<tr><td>"+str(produit.produit)+ "</td><td>"+str(produit.qte)+"</td></tr>"
            strTable = strTable+strRW
        
        strTable = strTable+"</tbody></table></body></html>"   
        hs = open("pdf.html", 'w')
        hs.write(strTable)

    def get(self,request,pk):
        self.generate_html_file(pk)
        pdfkit.from_file('pdf.html', 'Bon_Commande.pdf')
        pdf=open('Bon_Commande.pdf','rb')
        return FileResponse(pdf)

# sous Section BL
class Bl(APIView):
    serializer_class=BL_Serializer
    def get(self,request):
        BLs=BL.objects.all()
        serializer=BL_Serializer(BLs,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=JsonResponse().parse(request)
        serializer=BL_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Get_BL(APIView):
    serializer_class=BL_Serializer
    def get(self,request,pk):
        bl=BL.objects.get(id=pk)
        serializer=BL_Serializer(bl)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        bl = BL.objects.get(id=pk)
        bl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        bl=BL.objects.get(id=pk)
        data=JsonResponse().parse(request)
        serializer=BL_Serializer(bl,data=data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


# Section Stock
class Etat_Stock(APIView):
    def get(self,request):
        stock=Stock.objects.all()
        serializer=Stock_Serializer(stock,many=True)
        # print(serializer.data)
        Total_achat=0
        Total_vente=0
        for prd in serializer.data:
            Total_achat+=float(prd['unité_HT'])*int(prd['qte'])
            Total_vente+=float(prd['prix_vente'])*int(prd['qte'])
        print(Total_achat,Total_vente)
        return JsonResponse(serializer.data+[{'Total_achat':Total_achat},{'Total_vente':Total_vente}],safe=False)
class Entree_Stock_api(APIView):
    serializer_class=Entree_Stock_Serializer
    def get(self,request):
        entree_Stock=Entree_Stock.objects.all()
        serializer=Entree_Stock_Serializer(entree_Stock,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=JSONParser().parse(request)
        serializer=Entree_Stock_Serializer(data=data)
        if serializer.is_valid():
            prd=serializer.validated_data['produit']
            qte=serializer.validated_data['qte']
            try:
                stock=Stock.objects.filter(produit=prd)
            except Stock.DoesNotExist:
                stock = None
            if(stock):
                
                max=stock[0].qte
                i=0
                max_index=i
                for prd in stock:
                    if prd.qte>max:
                        max=prd.qte
                        max_index=i
                    i+=1
                stock[max_index].qte+=qte
                
                stock[max_index].save()
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            
            return Response([{'error':"produit n'exist pas dans le stock"}],status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Get_Entree_Stock_api(APIView):
    serializer_class=Entree_Stock_Serializer
    def get(self,request,pk):
        entree_Stock=Entree_Stock.objects.get(id=pk)
        serializer=Entree_Stock_Serializer(entree_Stock)
        return Response(serializer.data)
    def delete(self, request, pk):
        entree_Stock = Entree_Stock.objects.get(id=pk)
        entree_Stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        entree_Stock=Entree_Stock.objects.get(id=pk)
        data=JSONParser().parse(request)
        serializer=Entree_Stock_Serializer(entree_Stock,data=data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Sortie_Stock_api(APIView):
    serializer_class=Sortie_Stock_Serializer
    def get(self,request):
        entree_Stock=Sortie_Stock.objects.all()
        serializer=Sortie_Stock_Serializer(entree_Stock,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=JSONParser().parse(request)
        serializer=Sortie_Stock_Serializer(data=data)
        if serializer.is_valid():
            prd=serializer.validated_data['produit']
            qte=serializer.validated_data['qte']
            try:
                stock=Stock.objects.filter(produit=prd)
            except Stock.DoesNotExist:
                stock = None
            if(stock):
                
                max=stock[0].qte
                i=0
                max_index=i
                for prd in stock:
                    if prd.qte>max:
                        max=prd.qte
                        max_index=i
                    i+=1
                stock[max_index].qte-=qte
                if stock[max_index].qte<0:
                    return Response([{'error':"Cette quntite n'exist pas dans le stock"}],status=status.HTTP_400_BAD_REQUEST)
                stock[max_index].save()
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response([{'error':"produit n'exist pas dans le stock"}],status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Get_Sortie_Stock_api(APIView):
    serializer_class=Sortie_Stock_Serializer
    def get(self,request,pk):
        sortie_Stock=Sortie_Stock.objects.get(id=pk)
        serializer=Sortie_Stock_Serializer(sortie_Stock)
        return Response(serializer.data)
    def delete(self, request, pk):
        sortie_Stock = Sortie_Stock.objects.get(id=pk)
        sortie_Stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        sortie_Stock=Sortie_Stock.objects.get(id=pk)
        data=JSONParser().parse(request)
        serializer=Sortie_Stock_Serializer(sortie_Stock,data=data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# section Ventes
class Vente_un_Produit(APIView):
    serializer_class=Vente_Produit_Serializer
    def get(self,request):
        produit_vente=Vente_Produit.objects.all()
        serializer=Vente_Produit_Serializer(produit_vente,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=request.data
        serializer=Vente_Produit_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Get_Vente_Produit(APIView):
    serializer_class=Vente_Produit_Serializer
    def get(self,request,pk):
        produit_achete=Vente_Produit.objects.get(id=pk)
        serializer=Vente_Produit_Serializer(produit_achete)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        produit_vente = Vente_Produit.objects.get(id=pk)
        produit_vente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        produit_vente=Vente_Produit.objects.get(id=pk)
        serializer=Vente_Produit_Serializer(produit_vente,data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# Vente
class Ventes(APIView):
    serializer_class=Vente_Serializer
    def get(self,request):
        ventes=Vente.objects.all()
        serializer=Vente_Serializer(ventes,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=request.data
        serializer=Vente_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Get_Vente(APIView):
    serializer_class=Vente_Serializer
    def get(self,request,pk):
        vente=Vente.objects.get(id=pk)
        serializer=Vente_Serializer(vente)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        vente = Vente.objects.get(id=pk)
        vente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        vente=Vente.objects.get(id=pk)
        serializer=Vente_Serializer(vente,data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

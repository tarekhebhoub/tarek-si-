from django.urls import path
from . import apiviews
from . import views

urlpatterns = [
    path('produits/',apiviews.ListProduits.as_view()),
    path('produits/<int:pk>/',apiviews.GetProduit.as_view()),
    path('produits/imprimer/',apiviews.Imprimer_Produit.as_view()),
    path('types/',apiviews.ListType.as_view()),
    path('types/<int:pk>/',apiviews.GetType.as_view()),
    path('types/imprimer/',apiviews.Imprimer_Types.as_view()),
    path('clients/',apiviews.ListClient.as_view()),
    path('clients/<int:pk>/',apiviews.GetClient.as_view()),
    path('clients/imprimer/',apiviews.Imprimer_Clients.as_view()),
    path('fournisseurs/',apiviews.ListFournisseur.as_view()),
    path('fournisseurs/<int:pk>/',apiviews.GetFournisseur.as_view()),
    path('fournisseurs/imprimer/',apiviews.Imprimer_Fournisseurs.as_view()),
    path('commander_produits/',apiviews.Commander_Produits.as_view()),
    path('commander_produits/<int:pk>/',apiviews.Get_Commander_Produits.as_view()),
    path('commander_produits/<int:pk>/imprimer/',apiviews.Imprimer_Bon_Commande.as_view()),
    path('commander_produit/',apiviews.Commander_un_Produit.as_view()),
    path('commander_produit/<int:pk>/',apiviews.Get_Commander_un_Produit.as_view()),
    path('achete_un_produit/',apiviews.Acheter_un_Produit.as_view()),
    path('achete_un_produit/<int:pk>/',apiviews.Get_Acheter_un_Produit.as_view()),
    path('factures/',apiviews.Factures.as_view()),
    path('factures/<int:pk>',apiviews.Get_Facture.as_view()),
    path('BL/',apiviews.Bl.as_view()),
    path('BL/<int:pk>/',apiviews.Get_BL.as_view()),
    path('Ventes/',apiviews.Ventes.as_view()),
    path('Ventes/<int:pk>',apiviews.Get_Vente_Produit.as_view()),
    path('Vente_Produit/',apiviews.Vente_un_Produit.as_view()),
    path('Vente_Produit/<int:pk>',apiviews.Get_Vente_Produit.as_view()),
    path('stock/',apiviews.Etat_Stock.as_view()),
    path('entree_stock/',apiviews.Entree_Stock_api.as_view()),
    path('entree_stock/<int:pk>/',apiviews.Get_Entree_Stock_api.as_view()),
    path('sortie_stock/',apiviews.Sortie_Stock_api.as_view()),
    path('sortie_stock/<int:pk>/',apiviews.Get_Sortie_Stock_api.as_view()),

    # for the view
    path('add_client/',views.create_client)
]

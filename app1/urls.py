from django.urls import path
from . import apiviews

urlpatterns = [
    path('produits/',apiviews.ListProduits.as_view()),
    path('produits/<int:pk>',apiviews.GetProduit.as_view()),
    path('produits/imprimer',apiviews.Imprimer_Produit.as_view()),
    path('types/',apiviews.ListType.as_view()),
    path('types/<int:pk>',apiviews.GetType.as_view()),
    path('types/imprimer',apiviews.Imprimer_Types.as_view()),
    path('clients/',apiviews.ListClient.as_view()),
    path('clients/<int:pk>',apiviews.GetClient.as_view()),
    path('clients/imprimer',apiviews.Imprimer_Clients.as_view()),
    path('fournisseurs/',apiviews.ListFournisseur.as_view()),
    path('fournisseurs/<int:pk>',apiviews.GetFournisseur.as_view()),
    path('fournisseurs/imprimer',apiviews.Imprimer_Fournisseurs.as_view()),
]

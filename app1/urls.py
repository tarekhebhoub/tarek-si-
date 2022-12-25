from django.urls import path
from . import apiviews

urlpatterns = [
    path('produits/',apiviews.ListProduits.as_view()),
    path('produits/<int:pk>',apiviews.GetProduit.as_view())

]

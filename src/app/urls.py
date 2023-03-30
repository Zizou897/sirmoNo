from django.urls import path

from .api_views import *
from .views import *


urlpatterns = [

    #API documentation
    path('documentations/', index ),

    #API GROSSISTE MARCHE
    path('prix-marche-grosisiste/', PrixMarcheGrossisteMixin.as_view() ),
    path('prix-marche-grosisiste/<int:pk>/detail/', PrixMarcheGrossisteMixin.as_view() ),

    #API GROSSISTE MARCHE
    path('produit/', ProduitMixin.as_view() ),
    path('produit/<int:pk>/detail/', ProduitMixin.as_view() ),

    #API COLLECTE MARCHE
    path('collecte-marche/', PrixMarcheCollecteMixin.as_view() ),
    path('collecte-marche/<int:pk>/detail/', PrixMarcheCollecteMixin.as_view() ),


    #API ABONNE
    path('abonne/', AbonneMixin.as_view() ),
    path('abonne/<int:pk>/detail/', AbonneMixin.as_view() ),
]

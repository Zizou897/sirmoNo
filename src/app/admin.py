from django.contrib import admin

# Register your models here.
from app.models import *

@admin.register(Abonne)
class AbonneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'contact','statut')


@admin.register(PrixMarcheCollecte)
class PrixMarcheCollecteAdmin(admin.ModelAdmin):
    list_display = ('id_fiche', 'enquete', 'quantite_collecte','statut')

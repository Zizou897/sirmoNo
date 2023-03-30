from rest_framework import serializers

from app.models import *


class PrixMarcheGrossisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrixMarcheGrossiste
        fields = '__all__'


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class PrixMarcheCollecteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrixMarcheCollecte
        fields = '__all__'


class AbonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonne
        fields = '__all__'
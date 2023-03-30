from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver


from app.models import *

def index(request):

    template_name = 'app/index.html'
    return render(request, template_name)


@receiver(post_save, sender=PrixMarcheCollecte)
def new_data_added(sender, instance, created, **kwargs):
    if created:
        print("New data added!")
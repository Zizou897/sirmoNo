# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abonne(models.Model):
    nom = models.TextField(blank=True, null=True)
    prenom = models.TextField()
    speculation = models.TextField()
    prix = models.CharField(max_length=3)
    stock = models.CharField(max_length=3)
    debut = models.DateField()
    fin = models.DateField()
    adresse = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=20)
    statut = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    region = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'abonne'


class Acteur(models.Model):
    id_acteur = models.AutoField(primary_key=True)
    code_acteur = models.CharField(max_length=30)
    structure = models.CharField(max_length=20)
    categorie = models.TextField()
    sigle = models.CharField(max_length=100)
    nom_acteur = models.TextField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateTimeField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acteur'
        unique_together = (('id_acteur', 'code_acteur'), ('structure', 'code_acteur'),)


class AgendaPerso(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    expediteur = models.TextField(blank=True, null=True)
    titre = models.TextField()
    description = models.TextField(blank=True, null=True)
    all_day = models.IntegerField(blank=True, null=True)
    debut = models.DateTimeField()
    fin = models.DateTimeField()
    couleur = models.CharField(max_length=7, blank=True, null=True)
    lien = models.TextField(blank=True, null=True)
    valider = models.IntegerField()
    type = models.CharField(max_length=7)
    id_personnel = models.TextField()
    date_enregistrement = models.DateTimeField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agenda_perso'


class Annee(models.Model):
    annee = models.IntegerField(primary_key=True)
    plan = models.CharField(max_length=30)
    suivi = models.CharField(max_length=30)
    id_personnel = models.TextField()
    date_enregistrement = models.DateField()
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField()
    modifier_par = models.TextField()

    class Meta:
        managed = False
        db_table = 'annee'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutreMsg(models.Model):
    expediteur = models.TextField(blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autre_msg'


class Bulettin(models.Model):
    id_bulletin = models.AutoField(primary_key=True)
    nom = models.TextField()
    theme = models.CharField(max_length=11)
    date_debut = models.DateField()
    date_fin = models.DateField()
    description_bulletin = models.TextField(blank=True, null=True)
    id_personnel = models.CharField(max_length=30, blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    date_modification = models.DateField(blank=True, null=True)
    etat = models.CharField(max_length=30, blank=True, null=True)
    modifier_par = models.CharField(max_length=30, blank=True, null=True)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bulettin'


class Ca(models.Model):
    nom = models.TextField()
    prenom = models.TextField()
    contact = models.CharField(max_length=30, blank=True, null=True)
    fonction = models.TextField()
    description = models.TextField()
    region = models.IntegerField()
    adresse = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ca'


class CategorieProduit(models.Model):
    id_categorie_produit = models.AutoField(primary_key=True)
    code_categorie_produit = models.CharField(max_length=30)
    nom_categorie_produit = models.TextField()
    famille_produit = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'categorie_produit'


class ClasseAge(models.Model):
    id_classe = models.AutoField(primary_key=True)
    classe_age = models.CharField(max_length=30)
    espece_betail = models.TextField()

    class Meta:
        managed = False
        db_table = 'classe_age'


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom_client = models.TextField()
    adresse = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    localite = models.CharField(max_length=100, blank=True, null=True)
    type_client = models.IntegerField()
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField()
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Collecteur(models.Model):
    nom = models.TextField()
    prenom = models.TextField()
    sexe = models.TextField()
    contact = models.CharField(max_length=20)
    adresse = models.TextField()
    relai = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collecteur'


class Commune(models.Model):
    id_commune = models.AutoField(primary_key=True)
    code_commune = models.CharField(max_length=20)
    departement = models.CharField(max_length=20)
    nom_commune = models.TextField()
    abrege_commune = models.CharField(max_length=10, blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateTimeField()
    etat = models.CharField(max_length=10, blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commune'


class Connecter(models.Model):
    id_connexion = models.AutoField(primary_key=True)
    personnel = models.CharField(max_length=50)
    session_id = models.TextField(blank=True, null=True)
    date_connexion = models.DateTimeField()
    date_deconnexion = models.DateTimeField()
    date_c = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'connecter'


class Debarcadere(models.Model):
    id_debarcadere = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    nom = models.TextField()
    localite = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debarcadere'


class Departement(models.Model):
    id_departement = models.AutoField(primary_key=True)
    code_departement = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    nom_departement = models.TextField()
    abrege_departement = models.CharField(max_length=10, blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateTimeField()
    etat = models.CharField(max_length=10, blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departement'


class District(models.Model):
    id_district = models.AutoField(primary_key=True)
    sous_prefecture = models.IntegerField()
    nom_district = models.TextField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enquete(models.Model):
    id_enquete = models.AutoField(primary_key=True)
    marche = models.CharField(max_length=30)
    date_enquete = models.DateField()
    collecteur = models.IntegerField()
    statut = models.CharField(max_length=30, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete'


class EnqueteCollecte(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    marche = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_collecte'


class EnqueteConsommation(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    marche = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_consommation'


class EnqueteElevage(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    marche = models.CharField(max_length=100)
    periodicite = models.CharField(max_length=255, blank=True, null=True)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_elevage'


class EnqueteExportation(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    designation = models.TextField()
    quantite = models.FloatField(blank=True, null=True)
    prix = models.FloatField()
    unite = models.IntegerField()
    provenance = models.IntegerField()
    destination = models.IntegerField()
    nom_poste = models.IntegerField()
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_exportation'


class EnqueteGrossiste(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    marche = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_grossiste'


class EnqueteImportation(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    designation = models.TextField()
    quantite = models.FloatField(blank=True, null=True)
    prix = models.FloatField()
    unite = models.IntegerField()
    provenance = models.IntegerField()
    destination = models.IntegerField()
    nom_poste = models.IntegerField()
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_importation'


class EnquetePeche(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    debarcadere = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    nbr_barques_rentres_jour = models.IntegerField()
    volume_poissons_peches = models.FloatField(blank=True, null=True)
    principale_espece_peche = models.IntegerField(blank=True, null=True)
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_peche'


class EnqueteStocksMarchandsProduitsVegetauxLocaux(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    localite = models.CharField(max_length=20)
    nom_prenom = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    nature_produit = models.TextField(blank=True, null=True)
    unite = models.FloatField(blank=True, null=True)
    quantite = models.FloatField(blank=True, null=True)
    cout = models.FloatField(blank=True, null=True)
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_stocks_marchands_produits_vegetaux_locaux'


class EnqueteStocksProduitsAvicolesLocauxFermesAmeliorees(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    localite = models.CharField(max_length=20)
    ferme = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    nbr_pondeuses_presentes = models.FloatField(blank=True, null=True)
    nbr_poulets_chair_presents = models.FloatField(blank=True, null=True)
    nbr_oeufs_produits = models.FloatField(blank=True, null=True)
    nbr_poulets_reforme_vendues = models.FloatField(blank=True, null=True)
    nbr_poulets_chair_vendus = models.FloatField(blank=True, null=True)
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_stocks_produits_avicoles_locaux_fermes_ameliorees'


class EnqueteStocksSemencesVegetales(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    localite = models.CharField(max_length=20)
    nom_prenom = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    espece = models.TextField(blank=True, null=True)
    variete = models.TextField(blank=True, null=True)
    quantite = models.FloatField(blank=True, null=True)
    cout = models.FloatField(blank=True, null=True)
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_stocks_semences_vegetales'


class EnqueteTransfrontalier(models.Model):
    id_enquete = models.BigAutoField(primary_key=True)
    num_fiche = models.CharField(max_length=100)
    date_enquete = models.DateField()
    collecteur = models.CharField(max_length=30)
    designation = models.TextField()
    quantite = models.FloatField(blank=True, null=True)
    prix = models.FloatField()
    unite = models.IntegerField()
    provenance = models.IntegerField()
    destination = models.IntegerField(blank=True, null=True)
    nom_poste = models.IntegerField()
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquete_transfrontalier'


class Enqueteur(models.Model):
    id_enqueteur = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    nom = models.TextField()
    prenom = models.TextField()
    sexe = models.TextField()
    contact = models.CharField(max_length=20)
    localite = models.CharField(max_length=30)
    adresse = models.TextField(blank=True, null=True)
    superviseur = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    app_profil = models.CharField(max_length=255, blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enqueteur'


class EnvoiMsg(models.Model):
    region = models.TextField(blank=True, null=True)
    collecteur = models.IntegerField(blank=True, null=True)
    relai = models.IntegerField(blank=True, null=True)
    abonne = models.IntegerField(blank=True, null=True)
    radio = models.IntegerField(blank=True, null=True)
    ca = models.IntegerField(blank=True, null=True)
    uropc = models.IntegerField(blank=True, null=True)
    msg = models.TextField()
    date = models.DateTimeField()
    statut = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'envoi_msg'


class EspeceElevage(models.Model):
    id_espece_elevage = models.AutoField(primary_key=True)
    espece_elevage = models.CharField(max_length=100)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'espece_elevage'


class EspecePeche(models.Model):
    id_espece_peche = models.AutoField(primary_key=True)
    espece_peche = models.CharField(max_length=100)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'espece_peche'


class EtatCorporel(models.Model):
    id_etat = models.AutoField(primary_key=True)
    etat_corporel = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'etat_corporel'


class FamilleProduit(models.Model):
    id_famille_produit = models.AutoField(primary_key=True)
    code_famille_produit = models.CharField(max_length=30, blank=True, null=True)
    nom_famille_produit = models.TextField()
    affichage_ecran = models.IntegerField()
    date_enregistrement = models.DateField()
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'famille_produit'


class FicheCollecte(models.Model):
    id_fiche = models.AutoField(primary_key=True)
    enquete = models.IntegerField()
    statut = models.CharField(max_length=30, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fiche_collecte'


class Fonction(models.Model):
    id_fonction = models.AutoField(primary_key=True)
    fonction = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonction'


class FormeProduit(models.Model):
    id_forme_produit = models.AutoField(primary_key=True)
    code_forme_produit = models.CharField(max_length=30)
    nom_forme_produit = models.TextField()
    produit_concerne = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField()
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forme_produit'


class Fournisseur(models.Model):
    id_fournisseur = models.AutoField(primary_key=True)
    nom_fournisseur = models.TextField()
    adresse = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    localite = models.CharField(max_length=100, blank=True, null=True)
    type_fournisseur = models.IntegerField()
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField()
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fournisseur'


class Grossiste(models.Model):
    id_grossiste = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    nom = models.TextField()
    contact = models.CharField(max_length=20)
    localite = models.CharField(max_length=30)
    adresse = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grossiste'


class GroupeTache(models.Model):
    id_groupe_tache = models.AutoField(primary_key=True)
    jalon = models.IntegerField()
    id_activite = models.IntegerField()
    code_activite = models.CharField(max_length=30)
    annee = models.IntegerField()
    code_tache = models.IntegerField()
    proportion = models.FloatField(blank=True, null=True)
    proportion_reelle = models.FloatField()
    entite = models.IntegerField()
    intitule_tache = models.TextField(blank=True, null=True)
    debut = models.DateField(blank=True, null=True)
    fin = models.DateField(blank=True, null=True)
    periode = models.TextField(blank=True, null=True)
    cout_tache = models.FloatField(blank=True, null=True)
    n_lot = models.IntegerField()
    date_reelle = models.DateField(blank=True, null=True)
    observation = models.TextField(blank=True, null=True)
    projet = models.CharField(max_length=30)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)
    responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groupe_tache'


class IndicateurElevage(models.Model):
    id_indicateur_tache = models.AutoField(primary_key=True)
    intitule_indicateur_tache = models.TextField(blank=True, null=True)
    unite = models.CharField(max_length=30, blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicateur_elevage'


class IndicateursElevage(models.Model):
    id_indicateur = models.AutoField(primary_key=True)
    intitule_indicateur = models.TextField()
    unite_indicateur = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indicateurs_elevage'


class InfoSolde(models.Model):
    date = models.DateField(blank=True, null=True)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'info_solde'


class Localite(models.Model):
    nom = models.TextField()
    region = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'localite'


class Magasin(models.Model):
    id_magasin = models.AutoField(primary_key=True)
    nom = models.TextField()
    code = models.CharField(unique=True, max_length=30)
    localite = models.IntegerField()
    collecteur = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    capacite = models.FloatField()
    date_creation = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magasin'


class Marche(models.Model):
    id_marche = models.AutoField(primary_key=True)
    nom_marche = models.TextField()
    type_marche = models.TextField()
    code_marche = models.CharField(max_length=30)
    jour_marche = models.TextField()
    collecteur = models.TextField()
    localite = models.CharField(max_length=30)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    id_personnel = models.CharField(max_length=100, blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    modifier_par = models.CharField(max_length=100, blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marche'


class NiveauApprovisionement(models.Model):
    id_niveau_approvisionement = models.AutoField(primary_key=True)
    niveau_approvisionement = models.CharField(max_length=100)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'niveau_approvisionement'


class Parametrage(models.Model):
    projet = models.TextField()
    pays = models.TextField()
    adresse = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    slogan = models.TextField()
    activer_stock = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'parametrage'


class Pays(models.Model):
    id_pays = models.AutoField(primary_key=True)
    pays = models.CharField(max_length=100)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pays'


class PaysFrontalier(models.Model):
    id_pays = models.AutoField(primary_key=True)
    pays = models.CharField(max_length=100)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pays_frontalier'


class PaysProduit(models.Model):
    id_pays_produit = models.AutoField(primary_key=True)
    code_pays_produit = models.CharField(max_length=30)
    nom_pays_produit = models.TextField()
    region_produit = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pays_produit'


class Personnel(models.Model):
    n = models.AutoField(db_column='N', primary_key=True)  # Field name made lowercase.
    id_personnel = models.CharField(unique=True, max_length=200)
    titre = models.CharField(max_length=30, blank=True, null=True)
    pass_field = models.TextField(db_column='pass')  # Field renamed because it was a Python reserved word.
    nom = models.TextField()
    prenom = models.TextField()
    app_profil = models.CharField(max_length=1000, blank=True, null=True)
    contact = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    fonction = models.TextField()
    description_fonction = models.TextField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    niveau = models.IntegerField()
    date_enregistrement = models.DateField(blank=True, null=True)
    date_modification = models.DateField(blank=True, null=True)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'personnel'


class Postes(models.Model):
    id_postes = models.AutoField(primary_key=True)
    postes = models.CharField(max_length=255)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'postes'


class Prefecture(models.Model):
    id_prefecture = models.AutoField(primary_key=True)
    region = models.IntegerField()
    nom_prefecture = models.TextField()
    zoneopp = models.TextField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prefecture'


class PrixMarcheBordChamp(models.Model):
    id_fiche = models.AutoField(primary_key=True)
    produit = models.CharField(max_length=30)
    unite = models.TextField()
    poids_unitaire = models.FloatField()
    montant_achat = models.FloatField()
    prix_fg_kg = models.FloatField()
    localite_origine = models.IntegerField()
    distance_origine_marche = models.FloatField()
    montant_transport = models.FloatField()
    etat_route = models.CharField(max_length=100)
    client_principal = models.IntegerField()
    fournisseur_principal = models.IntegerField()
    quantite_collecte = models.FloatField()
    type_detaillant = models.CharField(max_length=100)
    statut = models.CharField(max_length=30, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prix_marche_bord_champ'


class PrixMarcheCollecte(models.Model):
    id_fiche = models.BigAutoField(primary_key=True)
    enquete = models.BigIntegerField()
    produit = models.CharField(max_length=100)
    unite = models.IntegerField()
    poids_unitaire = models.FloatField()
    montant_achat = models.FloatField()
    prix_fg_kg = models.FloatField()
    localite_origine = models.CharField(max_length=100)
    distance_origine_marche = models.FloatField()
    montant_transport = models.FloatField()
    etat_route = models.TextField()
    quantite_collecte = models.FloatField()
    client_principal = models.IntegerField()
    fournisseur_principal = models.IntegerField()
    niveau_approvisionement = models.IntegerField()
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    statut = models.IntegerField()
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prix_marche_collecte'


class PrixMarcheConsommation(models.Model):
    id_fiche = models.BigAutoField(primary_key=True)
    enquete = models.BigIntegerField()
    produit = models.CharField(max_length=100)
    unite = models.IntegerField()
    poids_unitaire = models.FloatField()
    prix_mesure = models.FloatField()
    prix_kg_litre = models.FloatField()
    niveau_approvisionement = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    document = models.TextField(blank=True, null=True)
    app_mobile = models.IntegerField()
    statut = models.IntegerField()
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prix_marche_consommation'


class PrixMarcheElevage(models.Model):
    id_fiche = models.BigAutoField(primary_key=True)
    enquete = models.BigIntegerField()
    bovins_stock_de_base = models.FloatField(blank=True, null=True)
    ovins_stock_de_base = models.FloatField(blank=True, null=True)
    caprins_stock_de_base = models.FloatField(blank=True, null=True)
    bovins_qty_debarque = models.FloatField(blank=True, null=True)
    ovins_qty_debarque = models.FloatField(blank=True, null=True)
    caprins_qty_debarque = models.FloatField(blank=True, null=True)
    bovins_stock_du_soir = models.FloatField(blank=True, null=True)
    ovins_stock_du_soir = models.FloatField(blank=True, null=True)
    caprins_stock_du_soir = models.FloatField(blank=True, null=True)
    bovins_qty_vendu = models.FloatField(blank=True, null=True)
    ovins_qty_vendu = models.FloatField(blank=True, null=True)
    caprins_qty_vendu = models.FloatField(blank=True, null=True)
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    statut = models.IntegerField()
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prix_marche_elevage'


class PrixMarcheElevageDetail(models.Model):
    id_fiche = models.BigAutoField(primary_key=True)
    enquete = models.BigIntegerField()
    vendeur = models.TextField(blank=True, null=True)
    localite_animaux_debarque = models.CharField(max_length=100)
    espece = models.IntegerField()
    nombre = models.FloatField(blank=True, null=True)
    vendus = models.FloatField()
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    statut = models.IntegerField()
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prix_marche_elevage_detail'


class PrixMarcheElevageEchantillon(models.Model):
    id_fiche = models.BigAutoField(primary_key=True)
    enquete = models.BigIntegerField()
    espece = models.IntegerField()
    classe_age = models.IntegerField()
    prix = models.FloatField(blank=True, null=True)
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    statut = models.IntegerField()
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prix_marche_elevage_echantillon'


class PrixMarcheElevageIndicateur(models.Model):
    id_fiche = models.BigAutoField(primary_key=True)
    enquete = models.BigIntegerField()
    indicateur = models.IntegerField()
    espece = models.IntegerField()
    nombre = models.FloatField(blank=True, null=True)
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    statut = models.IntegerField()
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prix_marche_elevage_indicateur'


class PrixMarcheGrossiste(models.Model):
    id_fiche = models.BigAutoField(primary_key=True)
    enquete = models.BigIntegerField(blank=True, null=True)
    grossiste = models.CharField(max_length=100, blank=True, null=True)
    produit = models.CharField(max_length=100)
    unite_stock = models.IntegerField()
    nombre_unite_stock = models.FloatField()
    poids_moyen_unite_stock = models.FloatField()
    poids_stock = models.FloatField()
    unite_achat = models.IntegerField()
    nombre_unite_achat = models.FloatField()
    poids_moyen_unite_achat = models.FloatField()
    poids_total_achat = models.FloatField()
    localite_achat = models.CharField(max_length=100)
    fournisseur_achat = models.IntegerField()
    unite_vente = models.IntegerField()
    nombre_unite_vente = models.FloatField()
    poids_moyen_unite_vente = models.FloatField()
    poids_total_unite_vente = models.FloatField()
    prix_unitaire_vente = models.FloatField()
    client_vente = models.IntegerField()
    localite_vente = models.CharField(max_length=100)
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    statut = models.IntegerField()
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prix_marche_grossiste'


class PrixMarchePecheEchantillon(models.Model):
    id_fiche = models.BigAutoField(primary_key=True)
    enquete = models.BigIntegerField()
    espece = models.IntegerField()
    um = models.IntegerField(blank=True, null=True)
    poids = models.FloatField(blank=True, null=True)
    pm = models.FloatField(blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)
    app_mobile = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    statut = models.IntegerField()
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prix_marche_peche_echantillon'


class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    code_produit = models.TextField(blank=True, null=True)
    nom_produit = models.TextField()
    famille_produit = models.IntegerField()
    affichage_ecran = models.IntegerField()
    date_enregistrement = models.DateField()
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produit'


class Projet(models.Model):
    id_projet = models.AutoField(primary_key=True)
    structure = models.CharField(max_length=10)
    code_projet = models.CharField(max_length=10)
    sigle_projet = models.TextField(blank=True, null=True)
    annee_debut = models.IntegerField(blank=True, null=True)
    annee_fin = models.IntegerField(blank=True, null=True)
    ugl = models.TextField(blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    intitule_projet = models.TextField()
    master = models.IntegerField()
    actif = models.IntegerField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projet'
        unique_together = (('code_projet', 'structure'),)


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    code_region = models.CharField(max_length=30)
    nom_region = models.TextField()
    abrege_region = models.CharField(max_length=30)
    region_naturelle = models.IntegerField(blank=True, null=True)
    couleur = models.TextField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class RegionNaturelle(models.Model):
    id_region_naturelle = models.AutoField(primary_key=True)
    nom_region_naturelle = models.TextField()

    class Meta:
        managed = False
        db_table = 'region_naturelle'


class RegionProduit(models.Model):
    id_region_produit = models.AutoField(primary_key=True)
    code_region_produit = models.CharField(max_length=30, blank=True, null=True)
    nom_region_produit = models.TextField()
    forme_concerne = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField()
    id_personnel = models.TextField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region_produit'


class RucheSync(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    code = models.TextField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateTimeField()
    etat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ruche_sync'


class Situation(models.Model):
    idid = models.IntegerField()
    contact = models.CharField(max_length=20)
    nombre = models.IntegerField()
    date = models.DateField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'situation'


class SousPrefecture(models.Model):
    id_sous_prefecture = models.AutoField(primary_key=True)
    prefecture = models.IntegerField()
    nom_sous_prefecture = models.TextField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    etat = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sous_prefecture'


class Structure(models.Model):
    id_structure = models.AutoField(primary_key=True)
    code_structure = models.CharField(unique=True, max_length=10)
    nom_structure = models.TextField()
    sigle = models.CharField(max_length=20, blank=True, null=True)
    slogan = models.TextField(blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    contact = models.TextField()
    info_plus = models.TextField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateTimeField()
    date_modification = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)
    statut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'structure'


class Test2(models.Model):
    id = models.IntegerField(primary_key=True)
    titre1 = models.TextField()
    titre2 = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_2'


class TypeDetaillant(models.Model):
    id_type_detaillant = models.AutoField(primary_key=True)
    type_detaillant = models.CharField(max_length=100)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_detaillant'


class Ugl(models.Model):
    id_ugl = models.AutoField(primary_key=True)
    structure = models.CharField(max_length=10)
    code_ugl = models.CharField(unique=True, max_length=10, blank=True, null=True)
    nom_ugl = models.TextField()
    abrege_ugl = models.CharField(max_length=10, blank=True, null=True)
    region_concerne = models.TextField(blank=True, null=True)
    chef_lieu = models.CharField(max_length=11)
    couleur = models.CharField(max_length=10)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateTimeField()
    etat = models.CharField(max_length=10, blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ugl'


class UniteMesure(models.Model):
    id_unite = models.AutoField(primary_key=True)
    nom_unite = models.CharField(max_length=100)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField()
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    poids_indicatif = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unite_mesure'


class UnitePeche(models.Model):
    id_unite_peche = models.AutoField(primary_key=True)
    unite_peche = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unite_peche'


class UserAccess(models.Model):
    id_personnel = models.IntegerField()
    page_edit = models.TextField()
    page_verif = models.TextField()
    page_valid = models.TextField()
    page_interd = models.TextField()
    personnel = models.IntegerField()
    date_enregistrement = models.DateField()
    date_modification = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_access'


class Village(models.Model):
    id_village = models.AutoField(primary_key=True)
    code_village = models.CharField(max_length=20)
    commune = models.CharField(max_length=20)
    nom_village = models.TextField()
    abrege_village = models.CharField(max_length=10, blank=True, null=True)
    homme = models.IntegerField(blank=True, null=True)
    femme = models.IntegerField(blank=True, null=True)
    jeune = models.IntegerField(blank=True, null=True)
    menage = models.IntegerField(blank=True, null=True)
    id_personnel = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateTimeField()
    etat = models.CharField(max_length=10, blank=True, null=True)
    modifier_par = models.TextField(blank=True, null=True)
    modifier_le = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'village'

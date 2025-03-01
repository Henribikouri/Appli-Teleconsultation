from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_doctor=models.BooleanField(default=False)
    is_agent=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
    
    # USER_TYPE_CHOICES = (
    #     ('patient', 'Patient'),
    #     ('agent', 'Agent communautaire'),
    #     ('doctor', 'Médecin'),
    # )

    # user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='patient')

from django.db import models

class CentreDeSante(models.Model):
    nom = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    centre_de_sante = models.ForeignKey(CentreDeSante, on_delete=models.CASCADE)
    numero_telephone = models.CharField(max_length=15)
    adresse = models.CharField(max_length=255)
    photo_profil = models.ImageField(upload_to='photos_profil/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
from django.db import models
from .models import Patient

class DonneesPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    age = models.IntegerField()
    poids = models.FloatField()
    temperature = models.FloatField()
    taille = models.FloatField()
    pression_arterielle = models.CharField(max_length=50)
    paludisme = models.BooleanField()
    vih = models.BooleanField()
    chlamydia = models.BooleanField()
    hepatite = models.BooleanField()
    taux_glycemie = models.FloatField()
    symptomes = models.TextField(blank=True, null=True)
    groupe_sanguin = models.CharField(max_length=3)
    mouvement_foetus = models.CharField(max_length=100)
    battement_coeur = models.CharField(max_length=100)
    hauteur_uterine = models.FloatField()
    date_derniere_regle = models.DateField()
    image_ecographie = models.ImageField(upload_to='images_ecographies/', blank=True, null=True)

    def __str__(self):
        return f'Donnees de {self.patient.user.username}'

from django.db import models
from django.utils import timezone

class Diagnostic(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_diagnostic = models.DateField(default=timezone.now)
    resultat = models.TextField()
    
    PRESCRIPTION_CHOICES = [
        ('Examen', 'Examen'),
        ('Medicament', 'Médicament'),
    ]
    prescription = models.CharField(max_length=10, choices=PRESCRIPTION_CHOICES)
    details = models.CharField(max_length=200)

    nom_docteur= models.CharField(max_length=200)
    def __str__(self):
        return f"Diagnostic de {self.patient.user.username} - {self.date_diagnostic}"


from django.db import models
from django.utils import timezone

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_rendezvous = models.DateField()
    heure_debut = models.TimeField()
    duree = models.DurationField()
    centre_de_sante = models.ForeignKey(CentreDeSante, on_delete=models.CASCADE)
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rendez-vous de {self.patient.user.username} le {self.date_rendezvous}"

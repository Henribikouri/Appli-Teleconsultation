from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import  get_user_model

User = get_user_model()
class UserForm(UserCreationForm):
    #user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',

        ]

from .models import CentreDeSante, Patient

# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ['nom', 'centre_de_sante', 'numero_telephone', 'adresse', 'photo_profil']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient

class PatientForm(UserCreationForm):
    centre_de_sante = forms.ModelChoiceField(queryset=CentreDeSante.objects.all(), required=True)
    numero_telephone = forms.CharField(max_length=15, required=True)
    adresse = forms.CharField(max_length=255, required=True)
    photo_profil = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=30, required=True, label="Prénom")
    last_name = forms.CharField(max_length=150, required=True, label="Nom de famille")
    email=forms.CharField(max_length=150, required=True, label="E-mail")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'centre_de_sante', 'numero_telephone','email', 'adresse', 'photo_profil')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            patient = Patient(
                user=user,
                centre_de_sante=self.cleaned_data['centre_de_sante'],
                numero_telephone=self.cleaned_data['numero_telephone'],
                adresse=self.cleaned_data['adresse'],
                photo_profil=self.cleaned_data['photo_profil']
            )
            patient.save()
        return user

from django import forms
from .models import DonneesPatient, Patient

class DonneesPatientForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all() ,label="Patient Choisit")
    class Meta:
        model = DonneesPatient
        fields = [
            'patient', 'age', 'poids', 'temperature', 'taille', 'pression_arterielle',
            'paludisme', 'vih', 'chlamydia', 'hepatite', 'taux_glycemie', 'symptomes',
            'groupe_sanguin', 'mouvement_foetus', 'battement_coeur', 'hauteur_uterine',
            'date_derniere_regle', 'image_ecographie'
        ]

    # def __init__(self, *args, **kwargs):
    #     super(DonneesPatientForm, self).__init__(*args, **kwargs)
    #     self.fields['patient'].queryset = Patient.objects.all()

    def clean_patient(self):
        patient = self.cleaned_data.get('patient')
        if DonneesPatient.objects.filter(patient=patient).exists():
            raise forms.ValidationError("Les données pour cette patiente ont déjà été enregistrées.")
        return patient

class PatienteForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['centre_de_sante', 'numero_telephone', 'adresse', 'photo_profil']

from django import forms
from .models import Diagnostic

class DiagnosticForm(forms.ModelForm):
    nom_docteur= forms.CharField(max_length=100, required=True, label="Par le Docteur :")
    class Meta:
        model = Diagnostic
        fields = ['date_diagnostic','prescription','details','resultat','nom_docteur']  # Exclure 'patient' et 'date_diagnostic' qui seront gérés automatiquement

from django import forms
from .models import RendezVous

from django import forms
from .models import RendezVous

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['date_rendezvous', 'heure_debut', 'duree', 'centre_de_sante', 'observation']
        widgets = {
            'date_rendezvous': forms.SelectDateWidget(),
            'heure_debut': forms.TimeInput(format='%H:%M'),
            'duree': forms.TimeInput(format='%H:%M'),
        }
        labels = {
            'date_rendezvous': 'Entrer la date du rendez-vous',
            'heure_debut': 'Heure du début',
            'duree': 'Durée du rendez-vous',
            'centre_de_sante': 'Centre de santé',
            'observation': 'Observation',
        }


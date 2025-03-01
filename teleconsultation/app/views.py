from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from app.forms import UserForm,DonneesPatientForm,PatientForm,PatienteForm
from .models import Patient

def home(request):
    error=''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_doctor:
                return redirect('doctor')
            elif user.is_agent:
                return redirect('agent')
            else:
                 return redirect('patient')
        else:
            error='Nom d’utilisateur ou mot de passe incorrect.'   
    return render(request, 'login.html', {'error': error})


def register(request):
    form = UserForm()
    if request.method == "POST":
        form=UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    return render(request, 'register.html', {'form': form})

@login_required
def patient(request):
    if not request.user.is_patient:
        return redirect('home')
    return render(request, 'patient.html')

@login_required
def agent(request):
    if not request.user.is_agent:
        return redirect('home')
    return render(request, 'agent.html')



@login_required
def doctor(request):
    if not request.user.is_doctor:
        return redirect('home')
    return render(request, 'doctor.html')


def logout(request):
    response = redirect('home')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    response['Clear-Site-Data'] = '"cache", "cookies", "storage", "executionContexts"'
    return response


from django.shortcuts import render, redirect
from .forms import PatientForm

@login_required
def ajouter_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agent')
    else:
        form = PatientForm()
    return render(request, 'ajouter_patient.html', {'form': form})


from .models import Patient

@login_required
def voir_patients(request):
    query = request.GET.get('q', '')
    if query:
        patients = Patient.objects.filter(
            user__last_name__icontains=query
        ) | Patient.objects.filter(
            centre_de_sante__nom__icontains=query
        )
    else:
        patients = Patient.objects.all()
    
    return render(request, 'voir_patients.html', {'patients': patients})


from django.shortcuts import render, get_object_or_404

from .models import Patient, DonneesPatient,Diagnostic

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    diagnostic = Diagnostic.objects.filter(patient=patient).first()
    diagnostic_existe = diagnostic is not None
    try:
        donnees_patiente = DonneesPatient.objects.get(patient=patient)
    except DonneesPatient.DoesNotExist:
        donnees_patiente = None

    return render(request, 'patient_detail.html', {
        'patient': patient,
        'donnees_patiente': donnees_patiente,
        'diagnostic_existe': diagnostic_existe,
        'diagnostic': diagnostic
    })


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient

@login_required
def supprimer_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.user.delete()  # Supprime également l'utilisateur associé
    messages.success(request, 'La patiente a été supprimée avec succès.')
    return redirect('voir_patients')

from django.shortcuts import render, redirect
from .forms import DonneesPatientForm

@login_required
def enregistrer_donnees_patiente(request):
    patient = Patient.objects.all()
    
    if request.method == 'POST':
        form = DonneesPatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_donnees')  # Redirigez vers une page de succès après l'enregistrement
    else:
        form = DonneesPatientForm()
    
    return render(request, 'enregistrer_donnees_patiente.html', {'form': form, 'patient': patient})

def success_donnees(request):
    return render(request, 'success_donnees.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm

def modifier_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        form = PatienteForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_detail', pk=patient.pk)  # Redirige vers la page des détails après la modification
    else:
        form = PatienteForm(instance=patient)

    return render(request, 'modifier_patient.html', {'form': form, 'patient': patient})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Diagnostic, Patient
from .forms import DiagnosticForm

def soumettre_diagnostic(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        form = DiagnosticForm(request.POST)
        if form.is_valid():
            diagnostic = form.save(commit=False)
            diagnostic.patient = patient  # Associer le diagnostic au patient
            diagnostic.save()
            return redirect('success_diagnostic')
    else:
        form = DiagnosticForm()
    
    return render(request, 'soumettre_diagnostic.html', {'form': form, 'patient': patient})


from django.shortcuts import render

def success_diagnostic(request):
    return render(request, 'success_diagnostic.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Diagnostic, Patient
from .forms import DiagnosticForm

def modifier_diagnostic(request, pk):
    diagnostic = get_object_or_404(Diagnostic, pk=pk)
    patient = diagnostic.patient  # Récupérer la patiente associée au diagnostic

    if request.method == 'POST':
        form = DiagnosticForm(request.POST, instance=diagnostic)
        if form.is_valid():
            form.save()
            return redirect('success_diagnostic')
    else:
        form = DiagnosticForm(instance=diagnostic)

    return render(request, 'modifier_diagnostic.html', {
        'form': form,
        'patient': patient
    })

def consulter_historique(request):
    patients = Patient.objects.all()
    
    # Calcul des statistiques pour le tableau de bord
    total_patients = patients.count()
    total_donnees = DonneesPatient.objects.count()
    
    # Ajouter le statut du diagnostic pour chaque patient
    patients_with_status = []
    for patient in patients:
        diagnostic = Diagnostic.objects.filter(patient=patient).first()
        if diagnostic:
            status = 'soumis'
            diagnostic_id = diagnostic.id
        else:
            status = 'en attente'
            diagnostic_id = None

        patients_with_status.append({
            'patient': patient,
            'status': status,
            'diagnostic_id': diagnostic_id,
        })
    
    context = {
        'patients_with_status': patients_with_status,
        'total_patients': total_patients,
        'total_donnees': total_donnees,
    }
    
    return render(request, 'consulter_historique.html', context)


def visualiser_diagnostic(request, diagnostic_id):
    diagnostic = get_object_or_404(Diagnostic, id=diagnostic_id)
    patient = diagnostic.patient  # On récupère la patiente associée au diagnostic

    # Vous pouvez passer d'autres données si nécessaire
    context = {
        'diagnostic': diagnostic,
        'patient': patient,
    }

    return render(request, 'visualiser_diagnostic.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .forms import RendezVousForm
from .models import Patient, RendezVous

def saisir_rendezvous(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rendezvous = form.save(commit=False)
            rendezvous.patient = patient
            rendezvous.save()
            return redirect('rendezvous_success', pk=patient.pk)  # Redirige vers la page de détail du patient
    else:
        form = RendezVousForm()

    return render(request, 'saisir_rendezvous.html', {'form': form, 'patient': patient})

from django.shortcuts import render

def rendezvous_success(request, pk):
    rendezvous = get_object_or_404(RendezVous, pk=pk)
    return render(request, 'rendezvous_success.html', {'rendezvous': rendezvous})

@login_required
def profil_patient(request):
    patient = get_object_or_404(Patient, user=request.user)
    return render(request, 'profil_patient.html', {'patient': patient})

from django.shortcuts import render, get_object_or_404
from .models import DonneesPatient, Patient

def voir_donnees_patient(request):
    # Récupérer l'utilisateur connecté
    user = request.user
    
    # Récupérer la patiente associée à cet utilisateur
    patient = get_object_or_404(Patient, user=user)
    
    # Récupérer les données associées à cette patiente
    donnees_patient = DonneesPatient.objects.filter(patient=patient)
    
    # Passer les données au template
    context = {
        'patient': patient,
        'donnees_patient': donnees_patient,
    }
    return render(request, 'voir_donnees_patient.html', context)

from django.shortcuts import render
from .models import Diagnostic

def liste_diagnostics(request):
    diagnostics = Diagnostic.objects.all()
    return render(request, 'liste_diagnostics.html', {'diagnostics': diagnostics})

def consulter_historiquedoctor(request):
    patients = Patient.objects.all()
    
    # Calcul des statistiques pour le tableau de bord
    total_patients = patients.count()

    total_donnees =patients.count()-Diagnostic.objects.count()
    
    # Ajoute le statut du diagnostic pour chaque patient
    patients_with_status = []
    for patient in patients:
        diagnostic = Diagnostic.objects.filter(patient=patient).first()
        if diagnostic:
            status = 'soumis'
            diagnostic_id = diagnostic.id
        else:
            status = 'en attente'
            diagnostic_id = None

        patients_with_status.append({
            'patient': patient,
            'status': status,
            'diagnostic_id': diagnostic_id,
        })
    
    context = {
        'patients_with_status': patients_with_status,
        'total_patients': total_patients,
        'total_donnees': total_donnees,
    }
    
    return render(request, 'consulter_historiquedoctor.html',context)

from django.shortcuts import render, get_object_or_404
from .models import Patient, Diagnostic, RendezVous

def mon_carnet(request):
    # Récupérer le patient connecté
    patient = get_object_or_404(Patient, user=request.user)

    # Récupérer la première prescription et rendez-vous du patient (s'il y en a)
    Diagnostique = Diagnostic.objects.filter(patient=patient).first()
    rendezvous = RendezVous.objects.filter(patient=patient).first()

    # Contexte pour rendre dans le template
    context = {
        'patient': patient,
        'Diagnostique': Diagnostique,
        'rendezvous': rendezvous,
    }

    return render(request, 'mon_carnet.html', context)

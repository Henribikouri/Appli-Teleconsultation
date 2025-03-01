from django.urls import path
from app.views import home,register,doctor,agent,patient,logout,ajouter_patient,voir_patients,patient_detail,supprimer_patient,enregistrer_donnees_patiente,success_donnees,modifier_patient,soumettre_diagnostic,success_diagnostic,modifier_diagnostic,consulter_historique,visualiser_diagnostic,saisir_rendezvous,rendezvous_success,profil_patient,voir_donnees_patient,consulter_historiquedoctor,liste_diagnostics,mon_carnet
from django.contrib.auth import views
urlpatterns = [
    path('',home, name="home"),
    path('register', register, name='register'),
    path('patient', patient, name='patient'),
    path('agent', agent, name='agent'),
    path('doctor',doctor, name='doctor'),
    path('logout', logout, name='logout'),
    path('ajouter_patient', ajouter_patient, name='ajouter_patient'),
    path('voir_patients', voir_patients, name='voir_patients'),
    path('patient/<int:pk>', patient_detail, name='patient_detail'),
    path('patient/supprimer/<int:pk>', supprimer_patient, name='supprimer_patient'),
    path('enregistrer_donnees_patiente', enregistrer_donnees_patiente, name='enregistrer_donnees_patiente'),
    path('success_donnees', success_donnees, name='success_donnees'),
    path('modifier_patient/<int:pk>', modifier_patient, name='modifier_patient'),
    path('soumettre_diagnostic/<int:pk>',soumettre_diagnostic, name='soumettre_diagnostic'),
    path('success-diagnostic',success_diagnostic, name='success_diagnostic'),
    path('modifier-diagnostic/<int:pk>', modifier_diagnostic, name='modifier_diagnostic'),
    path('consulter_historique', consulter_historique, name='consulter_historique'),
    path('diagnostic/<int:diagnostic_id>/', visualiser_diagnostic, name='visualiser_diagnostic'),
    path('saisir_rendezvous/<int:pk>/', saisir_rendezvous, name='saisir_rendezvous'),
    path('rendezvous/success/<int:pk>/', rendezvous_success, name='rendezvous_success'),
    path('profil/', profil_patient, name='profil_patient'),
    path('voir_donnees_patient', voir_donnees_patient, name='voir_donnees_patient'),
    path('diagnostics/',liste_diagnostics, name='liste_diagnostics'),
    path('historiquedoctor/',  consulter_historiquedoctor, name='consulter_historiquedoctor'),
    path('consulter_historique/<int:pk>',soumettre_diagnostic, name='soumettre_diagnostic'),
    path('mon_carnet/', mon_carnet, name='mon_carnet'),
    path('consulter_historique/<int:pk>',soumettre_diagnostic, name='soumettre_diagnostic'),
path('reset_password',views.PasswordResetView.as_view(template_name = 'password_reset.html'),name="reset_password"),
path('reset_password_send', views.PasswordResetDoneView.as_view(template_name = 'password_reset_sent.html'),name="password_reset_done"),
path('reset/<uidb64>/<token>',views.PasswordResetConfirmView.as_view(template_name = 'password_reset_form.html'),name="password_reset_confirm"),
path('reset_password_complete',views.PasswordResetCompleteView.as_view(template_name = 'password_reset_done.html'),name="password_reset_complete"),


]

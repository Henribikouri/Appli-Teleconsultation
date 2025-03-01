# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CentreDeSante, Patient,DonneesPatient,Diagnostic,RendezVous

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_doctor', 'is_agent', 'is_patient', 'last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_doctor', 'is_agent', 'is_patient', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )

class AdminCentreSante(admin.ModelAdmin):
    list_display = ('nom', 'zone')

class AdminDonneesPatient(admin.ModelAdmin):
    list_display = ('patient', 'age', 'poids', 'temperature', 'taille', 'pression_arterielle')


class AdminPatient(admin.ModelAdmin):
    list_display = ('get_username', 'get_first_name', 'get_last_name','get_email', 'centre_de_sante', 'numero_telephone', 'adresse')
    search_fields = ('user__username', 'numero_telephone')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Nom d\'utilisateur'

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'Prénom'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Nom de famille'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'E-mail'

class AdminDiagnostic(admin.ModelAdmin):
    list_display = ('patient', 'date_diagnostic', 'resultat', 'prescription','details','nom_docteur')
    list_filter = ('date_diagnostic', 'prescription')
    search_fields = ('patient__user__username', 'resultat')
    date_hierarchy = 'date_diagnostic'

class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_rendezvous', 'heure_debut', 'centre_de_sante', 'duree')
    list_filter = ('date_rendezvous', 'centre_de_sante')
    search_fields = ('patient__user__username', 'patient__user__last_name', 'patient__user__first_name')
    ordering = ('-date_rendezvous',)

    # Optionnel : pour personnaliser le formulaire d'administration
    fieldsets = (
        (None, {
            'fields': ('patient', 'date_rendezvous', 'heure_debut', 'duree', 'centre_de_sante', 'observation')
        }),
    )

# Enregistrer la configuration d'administration
admin.site.register(RendezVous, RendezVousAdmin)

admin.site.register(User, CustomUserAdmin)
admin.site.register(CentreDeSante, AdminCentreSante)
admin.site.register(Patient, AdminPatient)
admin.site.register(DonneesPatient, AdminDonneesPatient)
admin.site.register(Diagnostic, AdminDiagnostic)

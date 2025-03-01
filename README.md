## ICI, MON APPLICATION WEB DE TELECONSULTATION
Bienvenue , ici mon application web de téléconsultation développée avec Django durant mon stage de troisieme annee licence en science de l'ingenieur a l'ENSPY.
Cette application permet la gestion des consultations à distance entre patients, agents communautaires et médecins.

## 🛠 Technologies utilisées

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)  ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)  
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)  

## 🚀  Fonctionnalités principales
- Gestion des utilisateurs (Patients, Agents communautaires, Médecins)
- Attribution automatique des pages d'accueil selon le rôle de l'utilisateur
- Inscription et consultation des patientes par les agents
- Soumission et modification de diagnostics par les médecins
- Gestion des rendez-vous
- Interface ergonomique avec animations et couleurs attractives

## Technologies utilisées
- **Backend** : Django (Python)
- **Base de données** : SQlIite3
- **Frontend** : HTML, CSS, JavaScript (avec Bootstrap et des effets visuels avancés)
- **Authentification** : Django Authentication

## Installation et Configuration

### Prérequis
Assurez-vous d'avoir installé :
- Python 3.x
- Django
- MySQL (selon votre choix)
- Git

### 1. Cloner le projet
```bash
 git clone https://github.com/Henribikouri/Appli-Teleconsultation.git
 cd Appli-Teleconsultation
```

### 2. Créer et activer un environnement virtuel
```bash
python -m venv env
source env/bin/activate  # Sous Windows : env\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données
Modifiez le fichier **settings.py** pour définir votre base de données :
```python
DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 5. Appliquer les migrations et créer un superutilisateur
```bash
python manage.py migrate
python manage.py createsuperuser
```
Suivez les instructions pour créer un administrateur.

### 6. Démarrer le serveur
```bash
python manage.py runserver
```
Accédez à l'application via : [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Utilisation
### Accès à l'administration Django
Connectez-vous sur [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) avec le superutilisateur créé.

### Inscription et Connexion des Utilisateurs
- Les agents communautaires peuvent inscrire des patientes.
- Les médecins peuvent consulter les patientes et soumettre des diagnostics.

### Gestion des rendez-vous et diagnostics
- Un médecin peut ajouter un diagnostic avec prescriptions.
- Un patient peut consulter son historique et ses rendez-vous.

## Déploiement
Pour déployer l'application, utilisez un service comme **Heroku** ou **AWS** avec **Gunicorn** et une base de données distante.


## Contribution
Les contributions sont les bienvenues !
1. Forkez le projet
2. Créez une branche : `git checkout -b nouvelle-fonctionnalite`
3. Faites vos modifications et committez : `git commit -m 'Ajout d'une nouvelle fonctionnalité'`
4. Poussez la branche et créez une Pull Request

## Auteur
**BIKOURI HENRI** - henribikouri@gmail.com
## collaboration
**TAMEGUE DONALD** -
## Licence
Ce projet est sous licence MIT - voir le fichier **LICENSE** pour plus de détails prochainement.


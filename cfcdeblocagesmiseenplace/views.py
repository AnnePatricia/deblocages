from django.db import connection
import csv
from .models import dossier_de_pret
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from .utils import deblocage_authenticate


def home(request):

    if request.method == 'POST':
        deblocage_usermail = request.POST['deblocage-usermail']
        deblocage_password = request.POST['deblocage-password']

        user = deblocage_authenticate(
            email=deblocage_usermail, password=deblocage_password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Identifiants incorrects!')
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté')
    return redirect('home')


def dossier_detail(request, unitcode):
    # Récupérer un dossier spécifique par unitcode
    dossier = get_object_or_404(dossier_de_pret, unitcode=unitcode)

    # cleaned_unitcode = unitcode.replace('/', '-')
    # Transformer l'objet en dictionnaire pour le template
    data = {
        "UNITCODE": dossier.unitcode,
        "FULLNAME_": dossier.fullname,
        "CLIENTCODE_": dossier.clientcode,
        "PRODUCTCODE_": dossier.productcode,
        "REFERENCE_": dossier.reference,
        "CAPITALNOMINAL_": dossier.capitalnominal,
        "MAXTERM_": dossier.maxterm,
        "EXTERNALRIB_": dossier.externalrib,
        "EXTERNALRIBBANKCODE_": dossier.externalribbankcode,
        "STARTDATE_": dossier.startdate,
        "ENDDATE_": dossier.enddate,
        "RIB_": dossier.rib,
        "BANKCODE_": dossier.bankcode,
        "UDATE_": dossier.udate,
        "CDATE_": dossier.cdate,
        "FRANCHISEDURATION_": dossier.franchiseduration,
        "AGREEMENTDATE_": dossier.agreementdate,
        "DATEFIRSTALLOTEMENT_": dossier.datefirstallotement,
        "ECH_PREMI_": dossier.ech_premi,
    }
    
    
    # Passer les données au template
    return render(request, 'dossier_detail.html', {'data': data})


def home(request):
    # Récupérer tous les dossiers de prêt
    dossiers = dossier_de_pret.objects.all()
    
    # Transformer les objets en dictionnaires pour le template
    data = [
        {
            "unitcode": dossier.unitcode,
            "clientcode": dossier.clientcode,
            "fullname": dossier.fullname,
            "productcode": dossier.productcode,
            "reference": dossier.reference,
            "capitalnominal": dossier.capitalnominal,
            "maxterm": dossier.maxterm,
            "externalrib": dossier.externalrib,
            "externalribbankcode": dossier.externalribbankcode,
            "startdate": dossier.startdate,
            "enddate": dossier.enddate,
            "rib": dossier.rib,
            "bankcode": dossier.bankcode,
            "udate": dossier.udate,
            "cdate": dossier.cdate,
            "franchiseduration": dossier.franchiseduration,
            "agreementdate": dossier.agreementdate,
            "datefirstallotement": dossier.datefirstallotement,
            "ech_premi": dossier.ech_premi,
        }
        for dossier in dossiers
    ]
     # Redirige vers la page de connexion si l'utilisateur n'est pas connecté
    # Passer les données au template
    return render(request, 'home.html', {'data': data})



def read_csv(file_path):
    """
    Lit un fichier CSV avec un point-virgule comme séparateur.
    """
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')  # Spécifiez le délimiteur
        for row in reader:
            data.append(row)
    return data


def display_csv(request):
    """
    Vue pour afficher les données du CSV dans un template.
    """
    file_path = 'D:/deblocages/fichier_des_prets2.csv'  # Utilisez des barres obliques pour le chemin
    data = read_csv(file_path)
    return render(request, 'home.html', {'data': data})


def ma_vue(request):
    with connection.cursor() as cursor:
        # Passer une liste
        cursor.execute(
            "SELECT * FROM dossier_de_pret")
        rows = cursor.fetchall()
    return render(request, 'home.html', {'rows': rows})

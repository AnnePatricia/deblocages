import csv
from django.core.management.base import BaseCommand
from .models import Dossier_de_pret

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **kwargs):
        with open('D:/deblocages/fichier_des_prets2.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                Dossier_de_pret.objects.create(
                    unitcode=row['UNITCODE_'],
                    clientcode=row['CLIENTCODE_'],
                    fullname=row['FULLNAME_'],
                    productcode=row['PRODUCTCODE_'],
                    reference=row['REFERENCE_'],
                    capitalnominal=row['CAPITALNOMINAL_'],
                    maxterm=row['MAXTERM_'],
                    externalrib=row['EXTERNALRIB_'],
                    externalribbankcode=row['EXTERNALRIBBANKCODE '],
                    startdate=row['STARTDATE_'],
                    enddate=row['ENDDATE_'],
                    rib=row['RIB_'],
                    bankcode=row['BANKCODE_'],
                    udate=row['UDATE_'],
                    cdate=row['CDATE_'],
                    franchiseduration=row['FRANCHISEDURATION_'],
                    agreementdate=row['AGREEMENTDATE_'], 
                    datefirstallotement=row['DATEFIRSTALLOTEMENT_'],
                    ech_premi=row['ECH_PREMI_'],
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))


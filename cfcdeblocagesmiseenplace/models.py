from django.db import models


# Events type class model


class Type_evenement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return (f"{self.libele}")

# Next events class model


class Evenement_suivant(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return (f"{self.libele}")

# Events class model


class Evenement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    datedebut = models.CharField(max_length=100)
    datefin = models.CharField(max_length=100)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    typeevenement = models.ForeignKey(Type_evenement, on_delete=models.CASCADE)
    evenementsuivant = models.ForeignKey(
        Evenement_suivant, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.libele}")

# Alerts type class model


class Type_alerte(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return (f"{self.libele}")

# Alerts class model


class Alerte(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    declencheur = models.CharField(max_length=100)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    typealerte = models.ForeignKey(Type_alerte, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.libele}")

# Loan type class model


class Type_de_pret(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    productcode = models.CharField(max_length=100)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return (f"{self.libele}")

# Loan file class model


class dossier_de_pret(models.Model):
    unitcode = models.CharField(primary_key=True, max_length=100, db_column='UNITCODE')
    clientcode = models.CharField(max_length=100, db_column='CLIENTCODE')
    fullname = models.CharField(max_length=255, db_column='FULLNAME')
    productcode = models.CharField(max_length=100, db_column='PRODUCTCODE')
    reference = models.CharField(max_length=100, db_column='REFERENCE')
    capitalnominal = models.CharField(max_length=100, db_column='CAPITALNOMINAL')
    maxterm = models.CharField(max_length=100, db_column='MAXTERM')
    externalrib = models.CharField(max_length=100, db_column='EXTERNALRIB')
    externalribbankcode = models.CharField(max_length=100, db_column='EXTERNALRIBBANKCODE')
    startdate = models.DateField(db_column='STARTDATE')
    enddate = models.DateField(db_column='ENDDATE')
    rib = models.CharField(max_length=100, db_column='RIB')
    bankcode = models.CharField(max_length=100, db_column='BANKCODE')
    udate = models.DateField(db_column='UDATE')
    cdate = models.DateField(db_column='CDATE')
    franchiseduration = models.CharField(max_length=100, db_column='FRANCHISEDURATION')
    agreementdate = models.DateField(db_column='AGREEMENTDATE')
    datefirstallotement = models.DateField(db_column='DATEFIRSTALLOTEMENT')
    ech_premi = models.CharField(max_length=100, db_column='ECH_PREMI')


    def __str__(self):
        return (f"{self.fullname}")

# Loan conditions class model


class Conditions_primo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    libele = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    productcode = models.ForeignKey(Type_de_pret, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.libele}")



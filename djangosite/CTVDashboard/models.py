from django.db import models
class Names(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    class Meta:
        db_table = 'test_table'
        managed = False
class IR(models.Model):
    irKey = models.CharField(max_length=10000000000, primary_key=True)
    irNum = models.CharField(max_length=10000000000)
    extNum = models.CharField(max_length=10000000000)
    title = models.CharField(max_length=10000000000)
    PIs = models.CharField(max_length=10000000000)
    inventors = models.CharField(max_length=10000000000)
    TLO = models.CharField(max_length=10000000000)
    PLG = models.CharField(max_length=10000000000)
    submitted = models.CharField(max_length=10000000000)
    FY = models.BigIntegerField(max_length=10000000000)
    missing = models.CharField(max_length=10000000000)
    Review_Decision = models.CharField(max_length=10000000000)
    Disclosure_Status = models.CharField(max_length=10000000000)
    Technology_Status = models.CharField(max_length=10000000000)
    alert = models.CharField(max_length=10000000000)
    URL = models.CharField(max_length=10000000000)
    leadIRonWeb = models.BigIntegerField(max_length=10000000000)
    assessmentReceived = models.CharField(max_length=10000000000)
    disclosableTitle = models.CharField(max_length=10000000000)
    marketingAbstract = models.CharField(max_length=10000000000)
    fedFunding = models.BigIntegerField(max_length=10000000000)
    fedGrants = models.CharField(max_length=10000000000)
    relIRs = models.CharField(max_length=10000000000)
    stat = models.CharField(max_length=10000000000)
    ExNonexOpt_321 = models.FloatField(max_length=10000000000)

    class Meta:
        db_table = 'ir'
        managed = False

class PATENT(models.Model):
    docketKey1 = models.CharField(max_length=10000000000, primary_key=True)
    docketKeys = models.CharField(max_length=10000000000)
    app = models.CharField(max_length=10000000000)
    CC = models.CharField(max_length=10000000000)
    country = models.CharField(max_length=10000000000)
    appType = models.CharField(max_length=10000000000)
    title = models.CharField(max_length=10000000000)
    pubNum = models.CharField(max_length=10000000000)
    patNum = models.CharField(max_length=10000000000)
    file = models.CharField(max_length=10000000000)
    priority = models.CharField(max_length=10000000000)
    issue = models.CharField(max_length=10000000000)
    expiration = models.CharField(max_length=10000000000)
    abandon = models.CharField(max_length=10000000000)
    abandonVF = models.CharField(max_length=10000000000)
    origStatus = models.CharField(max_length=10000000000)
    status = models.CharField(max_length=10000000000)
    docket = models.CharField(max_length=10000000000)
    OLC = models.CharField(max_length=10000000000)
    IR1 = models.CharField(max_length=10000000000)
    IRs = models.CharField(max_length=10000000000)
    PI = models.CharField(max_length=10000000000)
    dept = models.CharField(max_length=10000000000)
    div = models.CharField(max_length=10000000000)
    patNumber = models.CharField(max_length=10000000000)
    deadDate = models.CharField(max_length=10000000000)
    staus = models.CharField(max_length=10000000000)
    alive = models.SmallIntegerField(max_length=10000000000)
    fileFY = models.CharField(max_length=10000000000)
    issueFY = models.CharField(max_length=10000000000)

    class Meta:
        db_table = 'patent'
        managed = False

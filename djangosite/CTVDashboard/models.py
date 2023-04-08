from django.db import models
class Names(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    class Meta:
        db_table = 'test_table'
        managed = False
    #agrrement num, ir num, won't need irkey
    #show on agreements when VAL=1
class IR(models.Model):
    irKey = models.CharField(max_length=1000, primary_key=True)
    irNum = models.CharField(max_length=1000)
    extNum = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    PIs = models.CharField(max_length=1000)
    inventors = models.CharField(max_length=1000)
    TLO = models.CharField(max_length=1000)
    PLG = models.CharField(max_length=1000)
    submitted = models.CharField(max_length=1000)
    FY = models.BigIntegerField(max_length=1000)
    missing = models.CharField(max_length=1000)
    Review_Decision = models.CharField(max_length=1000)
    Disclosure_Status = models.CharField(max_length=1000)
    Technology_Status = models.CharField(max_length=1000)
    alert = models.CharField(max_length=1000)
    URL = models.CharField(max_length=1000)
    leadIRonWeb = models.BigIntegerField(max_length=1000)
    assessmentReceived = models.CharField(max_length=1000)
    disclosableTitle = models.CharField(max_length=1000)
    marketingAbstract = models.CharField(max_length=1000)
    fedFunding = models.BigIntegerField(max_length=1000)
    fedGrants = models.CharField(max_length=1000)
    relIRs = models.CharField(max_length=1000)
    stat = models.CharField(max_length=1000)
    ExNonexOpt_321 = models.FloatField(max_length=1000)

    class Meta:
        db_table = 'ir'
        managed = False

class PATENT(models.Model):
    docketKey1 = models.CharField(max_length=1000, primary_key=True)
    docketKeys = models.CharField(max_length=1000)
    app = models.CharField(max_length=1000)
    CC = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    appType = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    pubNum = models.CharField(max_length=1000)
    patNum = models.CharField(max_length=1000)
    file = models.CharField(max_length=1000)
    priority = models.CharField(max_length=1000)
    issue = models.CharField(max_length=1000)
    expiration = models.CharField(max_length=1000)
    abandon = models.CharField(max_length=1000)
    abandonVF = models.CharField(max_length=1000)
    origStatus = models.CharField(max_length=1000)
    status = models.CharField(max_length=1000)
    docket = models.CharField(max_length=1000)
    OLC = models.CharField(max_length=1000)
    IR1 = models.CharField(max_length=1000)
    IRs = models.CharField(max_length=1000)
    PI = models.CharField(max_length=1000)
    dept = models.CharField(max_length=1000)
    div = models.CharField(max_length=1000)
    patNumber = models.CharField(max_length=1000)
    deadDate = models.CharField(max_length=1000)
    staus = models.CharField(max_length=1000)
    alive = models.SmallIntegerField(max_length=1000)
    fileFY = models.CharField(max_length=1000)
    issueFY = models.CharField(max_length=1000)

    class Meta:
        db_table = 'patent'
        managed = False

class AGREEMENT(models.Model):
    agtKey = models.CharField(max_length=1000, primary_key=True)
    agtNum = models.CharField(max_length=1000)
    alert = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    company = models.CharField(max_length=1000)
    conCMG = models.CharField(max_length=1000)
    conCompany = models.CharField(max_length=1000)
    conDept = models.CharField(max_length=1000)
    conDiv = models.CharField(max_length=1000)
    conPI = models.CharField(max_length=1000)
    conTLO = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    cuSUfy = models.CharField(max_length=1000)
    effective = models.CharField(max_length=1000)
    entityType = models.CharField(max_length=1000)
    execution = models.CharField(max_length=1000)
    expiration = models.CharField(max_length=1000)
    exportChecked = models.CharField(max_length=1000)
    irDept = models.CharField(max_length=1000)
    irDiv = models.CharField(max_length=1000)
    irInventor = models.CharField(max_length=1000)
    IRs = models.CharField(max_length=1000)
    leadSource = models.CharField(max_length=1000)
    metacat = models.CharField(max_length=1000)
    relAgtNum = models.CharField(max_length=1000)
    royalty = models.CharField(max_length=1000)
    startUp = models.CharField(max_length=1000)
    status = models.CharField(max_length=1000)
    termination = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    TLO = models.CharField(max_length=1000)
    totalValue = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    agtFY = models.FloatField(max_length=1000)
    equity = models.FloatField(max_length=1000)
    VAL = models.FloatField(max_length=1000)

    class Meta:
        db_table = 'patent'
        managed = False
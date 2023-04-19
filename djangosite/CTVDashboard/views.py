from datetime import date

from django.shortcuts import render
from django.urls import path
from .models import Names, IR, PATENT, AGREEMENT, INVENTOR


# Create your views here.
def index(request):
    irs = IR.objects.all()
    print(irs)
    patents = PATENT.objects.all()
    print(patents)
    agreements = AGREEMENT.objects.all()
    print(agreements)
    return render(request, 'CTVDashboard/index.html', {'irs': irs, 'patents': patents, 'agreements': agreements})

def example(request):
    # print("getting query")
    names = Names.objects.all()
    print(names)
    return render(request, 'CTVDashboard/example.html', {'names': names})


def ir(request):
    # print("getting query")
    irs = IR.objects.all()
    print(irs)
    return render(request, 'CTVDashboard/ir.html', {'irs': irs})

def patent(request):
    # print("getting query")
    patents = PATENT.objects.all()
    print(patents)
    return render(request, 'CTVDashboard/patent.html', {'patents': patents})

def agreement(request):
    # print("getting query")
    agreements = AGREEMENT.objects.all()
    print(agreements)
    return render(request, 'CTVDashboard/agreement.html', {'agreements': agreements})

def irstatistics(request):
    tabledata = IR.objects.filter(FY__gt=2007)
    persons = []
    for item in tabledata:
        if (item.TLO).__eq__("None"):
            continue
        if item.TLO not in persons:
            persons.append(item.TLO)
    years = range(2007, date.today().year + 1)
    listPeople = {}
    for person in persons: # create a dictionary for each person
        x = person
        print(x)
        x = {}
        print(x)
        for year in years: # go through every year
            print(year)
            for item in tabledata:  # go through each TLO in tabledata
                if (item.TLO).__eq__(person):
                    if year in x:
                        x[year] += 1
                    else:
                        x[year] = 0
        listPeople[person] = x
        print(x)
        print((listPeople[person]).get(2008))
    return render(request, 'CTVDashboard/irstatistics.html', {'listPeople': listPeople})

def agstatistics(request):
    tabledata = AGREEMENT.objects.filter(agtFY__gt=2007,VAL=1)
    persons = []
    for item in tabledata:
        if (item.TLO).__eq__("None"):
            continue
        if item.TLO not in persons:
            persons.append(item.TLO)
    years = range(2007, date.today().year + 1)
    listPeople = {}
    for person in persons: # create a dictionary for each person
        x = person
        print(x)
        x = {}
        print(x)
        for year in years: # go through every year
            print(year)
            for item in tabledata:  # go through each TLO in tabledata
                if (item.TLO).__eq__(person):
                    if year in x:
                        x[year] += 1
                    else:
                        x[year] = 0
        listPeople[person] = x
        print(x)
        print((listPeople[person]).get(2008))
    return render(request, 'CTVDashboard/agstatistics.html', {'listPeople': listPeople})

def agstatisticsOne(request):
    # print("getting query")
    agreementsOne = AGREEMENT.objects.filter(agtFY=2023,VAL=1)
    print(agreementsOne)
    return render(request, 'CTVDashboard/agstatisticsOne.html', {'agreementsOne': agreementsOne})

def inventor(request):
    # print("getting query")
    inventors = INVENTOR.objects.filter(lead=1)
    print(inventors)
    return render(request, 'CTVDashboard/inventor.html', {'inventors': inventors})

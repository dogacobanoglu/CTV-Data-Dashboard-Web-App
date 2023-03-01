from django.shortcuts import render
from django.urls import path
from .models import Names, IR, PATENT


# Create your views here.
def index(request):
    return render(request, "CTVDashboard/index.html",{})

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

from django.shortcuts import render
from django.db import transaction
from django.db.models import Q
from app.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def expert_user(request):
    if request.method == 'POST':
         with transaction.atomic():
            substance_obj = Substance(
                    atomic_number = request.POST['atomic_number'],
                    name = request.POST['name'],
                    symbol= request.POST['symbol'],
                    appearance = request.POST['appearance'],
                    atomic_mass = request.POST['atomic_mass'],
                    boil = request.POST['boil'],
                    category = request.POST['category'],
                    density = request.POST['density'],
                    discovered_by = request.POST['discovered_by'],
                    melt = request.POST['melt'],
                    molar_heat = request.POST['molar_heat'],
                    named_by = request.POST['named_by'],
                    period = request.POST['period'],
                    phase= request.POST['phase'],
                    characteristics= request.POST['characteristics'],
             )
            substance_obj.save()
    return render(request, 'expert_user.html')

def normal_user(request):
    substance_list = Substance.objects.all()
    if request.method == 'GET':
        this_searchkey = request.GET.get('searchkey')
        if this_searchkey:
            substance_list = Substance.objects.filter(
                Q(atomic_number__icontains=this_searchkey) |
                Q(name__icontains=this_searchkey) |
                Q(symbol__icontains=this_searchkey) |
                Q(appearance__icontains=this_searchkey) |
                Q(atomic_mass__icontains=this_searchkey) |
                Q(boil__icontains=this_searchkey) |
                Q(category__icontains=this_searchkey) |
                Q(density__icontains=this_searchkey) |
                Q(discovered_by__icontains=this_searchkey) |
                Q(melt__icontains=this_searchkey) |
                Q(molar_heat__icontains=this_searchkey) |
                Q(named_by__icontains=this_searchkey) |
                Q(period__icontains=this_searchkey) |
                Q(phase__icontains=this_searchkey) |
                Q(characteristics__icontains=this_searchkey)
            )
    context={
        'substance_list' : substance_list,
        #'search_result' : search_result,
    }
    return render(request, 'normal_user.html', context)
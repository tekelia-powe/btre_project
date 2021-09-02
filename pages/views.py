from django.shortcuts import render
from django.http import HttpResponse
from properties.choices import rent_choices, state_choices, bedroom_choices, city_choices

from properties.models import Property
from landlords.models import Landlord

def index(request):
    properties = Property.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'properties' : properties,
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'rent_choices' : rent_choices,
        'city_choices' : city_choices,
        
    }

    return render(request,'pages/index.html', context)

def about(request):
    # Get all landlords
    landlords = Landlord.objects.all

    context = {
        'landlords' : landlords
    }

    return render(request,'pages/about.html', context)
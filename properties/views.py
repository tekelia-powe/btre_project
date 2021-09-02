from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from properties.choices import rent_choices, state_choices, bedroom_choices,city_choices

from .models import Property

def index(request):
    properties = Property.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(properties,3)
    page = request.GET.get('page')
    paged_properties = paginator.get_page(page)
    context = {
        'properties' : paged_properties,
    }

    return render(request, 'properties/properties.html',context)

def property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)

    context = {
        'property': property
    }
    return render(request, 'properties/property.html', context)

def search(request):
    queryset_list = Property.objects.order_by('-list_date')

    # keyword 
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            queryset_list = queryset_list.filter(description__icontains=keyword)
    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    #Rent
    if 'rent' in request.GET:
        rent = request.GET['rent']
        if rent:
            queryset_list = queryset_list.filter(rent__lte=rent)
    
    context = {
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'rent_choices' : rent_choices,
        'city_choices' : city_choices,
        'properties' : queryset_list,
        'values' : request.GET
    }
    return render(request, 'properties/search.html', context)


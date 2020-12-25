from django.shortcuts import render
from .models import City, Property
from django.views.generic import ListView
from django.views import View


def is_valid_queryparam(param):
    return param != '' and param is not None


def BootstrapFilterView(request):
    qs = Property.objects.all()
    cities = City.objects.all()
    address_contains_query = request.GET.get('address_contains')
    size_query = request.GET.get('size')
    price_query = request.GET.get('price')
    city = request.GET.get('city')

    if is_valid_queryparam(address_contains_query):
        qs = qs.filter(address__icontains=address_contains_query)

    if is_valid_queryparam(size_query):
        qs = qs.filter(size__gt=size_query)

    if is_valid_queryparam(price_query):
        qs = qs.filter(price__gt=price_query)

    if is_valid_queryparam(city) and city != 'Choose...':
        qs = qs.filter(location__name=city)

    context = {
        'queryset': qs,
        'cities': cities
    }
    return render(request, 'bootstrap_form.html', context)


# classes below are used for demonstration purposes
class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        all_properties = Property.objects.all
        return render(request, self.template_name, {'all': all_properties})


class PropertyView(View):
    def get(self, request, *args, **kwargs):
        context = Property.objects.filter(location__name='Tallin')
        return render(request, 'tallin.html', {'context': context})


class PropertyListView(ListView):
    template_name = 'property_list.html'
    queryset = Property.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)
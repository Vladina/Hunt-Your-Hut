from django.shortcuts import render, get_object_or_404
from .models import City, Property
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView
)
from .forms import PropertyForm
from django.views import View


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        all_properties = Property.objects.all
        return render(request, 'home.html', {'all': all_properties})

class PropertyView(View):
    def get(self, request, *args, **kwargs):
        context = Property.objects.filter(location__name='Tallin')
        return render(request, 'tallin.html', {'context': context})


class PropertyCreateView(CreateView):
    template_name = 'property_create.html'
    form_class = PropertyForm
    queryset = Property.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/'


class PropertyListView(ListView):
    template_name = 'property_list.html'
    queryset = Property.objects.all()


class PropertyDetailView(DetailView):
    template_name = 'property_detail.html'
    queryset = Property.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Property, id=id_)


class PropertyUpdateView(UpdateView):
    template_name = 'property_create.html'
    form_class = PropertyForm
    queryset = Property.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Property, id=id_)

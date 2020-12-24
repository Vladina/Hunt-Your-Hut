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
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        all_properties = Property.objects.all
        return render(request, self.template_name, {'all': all_properties})


class PropertyView(View):
    def get(self, request, *args, **kwargs):
        context = Property.objects.filter(location__name='Tallin')
        return render(request, 'tallin.html', {'context': context})


class PropertyCreateView(CreateView):
    template_name = 'property_create.html'

    def get(self, request, *args, **kwargs):
        form = PropertyForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            form = PropertyForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class PropertyListView(ListView):
    template_name = 'property_list.html'
    queryset = Property.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


class CustomPropertyView(PropertyListView):
    template_name = 'property_create.html'
    queryset = Property.objects.filter(location__name="Kiev")


class PropertyDetailView(DetailView):
    template_name = 'property_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Property, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)




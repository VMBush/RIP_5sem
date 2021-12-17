from django.shortcuts import get_object_or_404, render
from django.views import generic


from .models import Kit, Shelter

# Create your views here.


class KitListView(generic.ListView):
    model = Kit

    def get_queryset(self):
        return Kit.objects.filter(shelter__exact=self.kwargs['sh'])

    def get_context_data(self, **kwargs):
        context = super(KitListView, self).get_context_data(**kwargs)
        context['sh'] = self.kwargs['sh']
        context['shelter'] = Shelter.objects.get(id=self.kwargs['sh'])
        return context


class KitDetailView(generic.DetailView):
    model = Kit

    def get_context_data(self, **kwargs):
        context = super(KitDetailView, self).get_context_data(**kwargs)
        context['sh'] = Kit.objects.get(id=self.kwargs['pk']).shelter.id
        context['shelter'] = Kit.objects.get(id=self.kwargs['pk']).shelter
        return context


class ShelterListView(generic.ListView):
    model = Shelter

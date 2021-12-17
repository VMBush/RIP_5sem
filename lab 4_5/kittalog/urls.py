from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path("", views.ShelterListView.as_view(), name='shelter_list'),
    path("<int:sh>", views.KitListView.as_view(),  name='kittalog'),
    path("kit/<int:pk>", views.KitDetailView.as_view(), name='kit_detail')

]

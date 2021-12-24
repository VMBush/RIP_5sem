from django.urls import include, path
from . import views
from django.views.generic import RedirectView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'kittalog', views.KitViewSet)

urlpatterns = [
    path("", views.ShelterListView.as_view(), name='shelter_list'),
    path("<int:sh>", views.KitListView.as_view(),  name='kittalog'),
    path("kit/<int:pk>", views.KitDetailView.as_view(), name='kit_detail'),
    path("rout/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls, namespace='rest_framework')),

]

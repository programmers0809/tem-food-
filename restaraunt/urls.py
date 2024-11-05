from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('menu/', MenuView.as_view(), name='menu_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('service/', ServiceView.as_view(), name='service_page'),
    path('team/', TeamView.as_view(), name='team_page'),
]

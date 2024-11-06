from django.shortcuts import render

from django.views import View
from .models import CategoryModel, ProductsModel, OpeningHours

class HomeView(View):
    def get(self, request):
        
        category_list = CategoryModel.objects.all()
        fast_food_list = ProductsModel.manager.all().filter(category__name='Fast-food').order_by('-publish_time')
        drinks_list = ProductsModel.manager.all().filter(category__name='Ichimliklar').order_by('-publish_time')
        ice_cream_list = ProductsModel.manager.all().filter(category__name='Muzqaymoqlar').order_by('-publish_time')
        opening_hours_list = OpeningHours.objects.all()
        
        
        context = {
            'category_list' : category_list,
            'fast_food_list' : fast_food_list,
            'drinks_list' : drinks_list,
            'ice_cream_list' : ice_cream_list,
            'opening_hours_list' : opening_hours_list,  
        }
    
        return render(request, 'home.html', context)
    
    
class MenuView(View):
    def get(self, request):
        
        category_list = CategoryModel.objects.all()
        fast_food_list = ProductsModel.manager.all().filter(category__name='Fast-food').order_by('-publish_time')
        drinks_list = ProductsModel.manager.all().filter(category__name='Ichimliklar').order_by('-publish_time')
        ice_cream_list = ProductsModel.manager.all().filter(category__name='Muzqaymoqlar').order_by('-publish_time')
        
        context = {
            'category_list' : category_list,
            'fast_food_list' : fast_food_list,
            'drinks_list' : drinks_list,
            'ice_cream_list' : ice_cream_list,
        }
        
        return render(request, 'menu.html', context=context)

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    
class ServiceView(View):
    def get(self, request):
        return render(request, 'service.html')

class TeamView(View):
    def get(self, request):
        return render(request, 'team.html')

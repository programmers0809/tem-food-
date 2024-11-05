from django.shortcuts import render

from django.views import View
from .models import CategoryModel, ProductsModel

class HomeView(View):
    def get(self, request):
        
        category_list = CategoryModel.objects.all()
        # fast_food_list = ProductsModel.manager.all().filter(category__name='Fast-food').order_by('-publish_time')
        
        
        context = {
            'category_list' : category_list,
        }
    
        return render(request, 'home.html', context)
    
    
class MenuView(View):
    def get(self, request):
        return render(request, 'menu.html')

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

from django.shortcuts import render

from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
    
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

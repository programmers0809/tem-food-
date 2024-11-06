from django.contrib import admin

from .models import *

admin.site.register(CategoryModel)
admin.site.register(ProductsModel)
admin.site.register(OpeningHours)

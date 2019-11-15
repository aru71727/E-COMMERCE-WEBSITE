from django.contrib import admin

# Register your models here.
from .models import Offers
from .models import Product

admin.site.register(Offers)
admin.site.register(Product)

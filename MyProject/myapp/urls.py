from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('deals/',views.deals, name = 'deals'),
    path("products/<int:myid>", views.productView, name="ProductView"),


]
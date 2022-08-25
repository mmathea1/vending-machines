"""vending_machines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from machines.views import CoinsAvailableViewSet, ProductViewSet, VendingMachineViewSet

router = routers.DefaultRouter()
router.register(r'machines', VendingMachineViewSet)
router.register(r'coins', CoinsAvailableViewSet)
router.register(r'products', ProductViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),

    # POST ability to create vending machine /machine/create
    # ability to view vending machine /machine/<pk> {name, location}
    # ability to add available coins to machine /machine/coins/
    # ability to add products to machine /machine/product/
]
urlpatterns += router.urls

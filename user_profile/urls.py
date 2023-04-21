from django.urls import path
from .views import ProdCat

app_name = 'store'

urlpatterns = [
path('',ProdCat.as_view(), name ='allProdCat'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi,name='home-page'),
    path('contacts',views.hlo,name='contacts'),
    path('products',views.hm,name='products'),
]
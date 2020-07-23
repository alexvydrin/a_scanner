from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('engines/', views.engines, name='engines'),
    path('markets/', views.markets, name='markets'),
    path('securities/', views.securities, name='securities'),
]

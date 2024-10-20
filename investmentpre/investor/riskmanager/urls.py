from django.urls import path
from . import views

urlpatterns = [
    path('risk/risk-rate/', views.risk_rate, name='risk_rate'),
    path('formInfo/', views.formInfo, name='formInfo'),
    path('gold/', views.gold, name='gold'),
    ]
from django.urls import path
from . import views
urlpatterns = [
    path('golresult/', views.golresult, name='golresult'),
    path('goldy/', views.goldy, name='goldy'),
]

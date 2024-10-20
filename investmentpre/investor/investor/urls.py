from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('integrator.urls')), 
    path('risk/', include('riskmanager.urls')),
    path('go/', include('goldy.urls')),
]

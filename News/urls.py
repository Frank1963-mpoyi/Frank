
from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    #path('', include('mpoyi.urls')),
    path('', include('mitongo.urls')),
    path('admin/', admin.site.urls),
]

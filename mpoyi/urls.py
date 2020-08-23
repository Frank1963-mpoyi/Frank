
from django.urls import path
from .views import paul_draft


urlpatterns = [
    path('draft', paul_draft),
    ]

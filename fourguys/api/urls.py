from django.urls import path
from .views import initialize

urlpatterns = [
    path('', initialize),
]
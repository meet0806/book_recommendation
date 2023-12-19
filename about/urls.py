from django.urls import path
from about.views import AboutUs

urlpatterns = [
    path('', AboutUs, name='About')
]

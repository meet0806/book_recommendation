from Bootwork.views import Main, Sum
from django.urls import path, include

urlpatterns = [
    path('', Main,name='Home'),
    path('getbook', Sum,name='Recommendation')
]

from django.urls import path
from graph.views import Graph, Graph1, Graph2

urlpatterns = [
    path('', Graph, name='Chart'),
    path('graph1/', Graph1, name='Chart_1'),
    path('graph2/', Graph2, name='Chart_2'),
]

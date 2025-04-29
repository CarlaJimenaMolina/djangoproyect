from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listar_productos, name= 'listar_productos'),
    path('pedidos/', views.crear_pedido, name= 'crear_pedido')
]
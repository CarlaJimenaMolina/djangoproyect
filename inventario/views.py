from django.http import JsonResponse
from .models import Producto, Item, Pedido
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def listar_productos(request):
    if request.method == 'GET':
        productos = list(Producto.objects.values())
        return JsonResponse(productos, safe=false)
    else:
        return JsonResponse({'Solo se permiten métodos de consulta GET'})
    
@csrf_exempt
def crear_pedido(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)
        except:
            return JsonResponse({'error': 'Json inválido'}, status =400)
        
        user_id = datos.get('user_id')
        if not user_id:
            return JsonResponse({'error': 'Se requiere un user_id'})
        
        items = datos.get('items')
        if not items:
            return JsonResponse({'error': 'Se requiere al menos un item'})

        try:
            user = User.objects.get(id = user_id)
        except User.DoesNotExist:
            return JsonResponse({'error','El usuario seleccionado no existe'}, status= 404)
        pedido = Pedido.objects.create(user = user)
        for item in items:
            producto_id = item.get('producto_id')
            if not producto_id:
                return JsonResponse({'error','Se debe ingresar un id de producto en el item'}, status= 404)
            cantidad =item.get('cantidad')
            if not cantidad:
                return JsonResponse({'error','Se debe ingresar la cantidad de producto solicitado'}, status= 404)
            
            try:
                producto = Producto.objects.get(id =producto_id)
            except producto.DoesNotExist:
                return JsonResponse({'error','El roducto seleccionado no existe'}, status= 404)

            if producto.stock < cantidad:
                return JsonResponse({'error','No hay stock suficiente del productoseleccionado'}, status= 404)
            
            producto.stock -= cantidad
            producto.save()

            Item.objects.create(pedido =pedido, producto= producto, cantidad=cantidad)
        return JsonResponse({'Pedido creado exitosamente'})
    
    else:
        return JsonResponse({'Solo se permiten métodos de consulta GET'})
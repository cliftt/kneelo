from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Order

def homepage(request):
    return render(request, 'main.html')  # имя файла должно быть 'main.html'

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Order.objects.create(
            name=data.get('name'),
            phone=data.get('phone'),
            email=data.get('email'),
            address=data.get('address')
        )
        return JsonResponse({'message': 'Order created successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

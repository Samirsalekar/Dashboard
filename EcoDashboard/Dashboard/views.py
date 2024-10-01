from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from Dashboard.models import Order
from django.core import serializers

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
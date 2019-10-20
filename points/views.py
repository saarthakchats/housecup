from django.shortcuts import render, get_object_or_404
from .models import House

# Create your views here.
def home(request):
	ranked = House.objects.order_by('points')
	return render(request, 'points/home.html', {'first': ranked[3], 'second': ranked[2], 'third': ranked[1], 'fourth': ranked[0]})

def update(request):
	return render(request, 'points/update.html')

def housepage(request, house_name):
	house = get_object_or_404(House, mascot=house_name)
	return render(request, 'points/housepage.html', {'house': house})

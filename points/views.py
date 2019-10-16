from django.shortcuts import render
from .models import House

# Create your views here.
def home(request):
	ranked = House.objects.order_by('points')
	return render(request, 'points/home.html', {'first': ranked[3], 'second': ranked[2], 'third': ranked[1], 'fourth': ranked[0]})

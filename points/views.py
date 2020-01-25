from django.shortcuts import render, get_object_or_404, redirect
from .models import House
import datetime


# Create your views here.
def home(request):
	ranked = House.objects.order_by('points')
	return render(request, 'points/home.html', {'first': ranked[3], 'second': ranked[2], 'third': ranked[1], 'fourth': ranked[0]})

def update(request):
	if request.method == 'POST':
		if request.POST['secret'] == '39ht$jio7k':
			house = get_object_or_404(House, mascot=request.POST['housename'])
			house.points += int(request.POST['points'])
			if request.POST['category'] == 'sports':
				house.sports += int(request.POST['points'])
			elif request.POST['category'] == 'academics':
				house.academics += int(request.POST['points'])
			elif request.POST['category'] == 'achievements':
				house.achievements += int(request.POST['points'])
			elif request.POST['category'] == 'miscellaneous':
				house.miscellaneous += int(request.POST['points'])
			elif request.POST['category'] == 'competitions':
				house.competitions += int(request.POST['points'])
			house.save()
			return render(request, 'points/update.html', {'error': 'Points Updated'})
		else:
			return render(request, 'points/update.html', {'error': 'Incorrect Key'})
	return render(request, 'points/update.html')

def housepage(request, house_name):
	house = get_object_or_404(House, mascot=house_name)
	return render(request, 'points/housepage.html', {'house': house})

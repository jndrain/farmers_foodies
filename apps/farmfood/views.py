from django.shortcuts import render, redirect
from .models import Course 

def index(request):
	context = {
		"farmers": farmers.objects.all()
	}
	return render(request, "farmfood.html", context)

def login(request):
	farmers.objects.create(name = request.POST['name'], description = request.POST['description'])
	return redirect("farmfood/dashboard")

def update(request, id):
	farmers = farmers.objects.get(id=id)
	if request.method =='POST':
		farmer.objects.update_or_create(blah="blah", blah="blah")
		return redirect('/')
	else:
		context = {
			"farmers": farmers
		}
		return render(request, "farmfood/delete.html", context)
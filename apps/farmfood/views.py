from django.shortcuts import render, redirect
from .models import Course 

def index(request):
	context = {
		"farmers": farmers.objects.all()
	}
	return render(request, "farmfood.html", context)

def login_Register(request):
	farmers.objects.create(name = request.POST['name'], description = request.POST['description'])
	return 

def destroy(request, id):
	farmers = farmers.objects.get(id=id)
	if request.method =='POST':
		farmer.delete()
		return redirect('/')
	else:
		context = {
			"farmers": farmers
		}
		return render(request, "farmfood/delete.html", context)
from django.shortcuts import render, redirect
from .models import Course 

def index(request):
	context = {
		"courses": Course.objects.all()
	}
	return render(request, "farmfood.html", context)

def create(request):
	farmers.objects.create(name = request.POST['name'], description = request.POST['description'])
	return stuff

def destroy(request, id):
	farmers = farmers.objects.get(id=id)
	if request.method =='POST':
		farmer.delete()
		return redirect('/')
	else:
		context = {
			"farmer": farmer
		}
		return render(request, "course/delete.html", context)
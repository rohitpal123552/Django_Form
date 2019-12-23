from django.shortcuts import render, redirect
from myform.models import Person
from .forms import PersonForm

# Create your views here.

def home(request):
	persons = Person.objects.all()
	return render(request, 'home.html', {'persons':persons})


def add_person(request):
	if request.method == "POST":
		form = PersonForm(request.POST)
		if form.is_valid():
			person = form.save()
			return redirect('home')
	else:
		form = PersonForm()
	return render(request, 'add_person.html', {'form':form})
		
	
	
	
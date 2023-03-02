from django.shortcuts import render
from .models import Notes
from .forms import MakeNewNote

# Create your views here.


def home(response):
	return render(response, 'main/home.html', {})

def create(response):
	if response.method == "POST":
		form=MakeNewNote(response.POST)
		if form.is_valid():
			n = form.cleaned_data["text"]
			note = Notes()
			note.text = n
			note.save()
		return render(response, 'main/singlenote.html', {"note":note})
	else:
		form=MakeNewNote()
	return render(response, 'main/create.html', {"form":form})

def mynotez(response):
	noteslist=Notes.objects
	return render(response, 'main/mynotez.html', {"noteslist":noteslist})

def singlenote(response, id):
 	n = Notes.objects.get(id=id)
 	return render(response, "main/singlenote.html", {"text":n.text})
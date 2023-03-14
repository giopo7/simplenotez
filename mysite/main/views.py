from django.shortcuts import render
from .models import Notes
from .forms import MakeNewNote
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def home(response):
	return render(response, 'main/home.html', {})

def create(request):
	if request.method == "POST":
		form=MakeNewNote(request.POST)
		if form.is_valid():
			n = form.cleaned_data["text"]
			note = Notes()
			note.text = n
			note.user = request.user
			note.save()
		return render(request, 'main/singlenote.html', {"note":note})
	else:
		form=MakeNewNote()
	return render(request, 'main/create.html', {"form":form})

def mynotez(request):
	# noteslist=Notes.objects
	if request.user.is_authenticated:
		noteslist = Notes.objects.filter(user=request.user)
		return render(request, 'main/mynotez.html', {"noteslist":noteslist})
	else:
		return render(request, 'main/create.html', {} )

def delete_note(request, id):
    query = Notes.objects.get(id=id)
    query.delete()
    return mynotez(request)


def singlenote(response, id):
 	n = Notes.objects.get(id=id)
 	return render(response, "main/singlenote.html", {"text":n.text})
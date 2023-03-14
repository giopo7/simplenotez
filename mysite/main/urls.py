from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="Home"),
	path("home/", views.home, name="Home"),
	path("create/", views.create, name="Create"),
	path("mynotez/", views.mynotez, name="MyNoteZ"),
	path("<int:id>", views.singlenote, name="Single Note"),
	path("delete/<int:id>", views.delete_note, name="Delete Note"),
	]
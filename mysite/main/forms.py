from django import forms 

class MakeNewNote(forms.Form):
	text = forms.CharField(label="text", max_length=500)
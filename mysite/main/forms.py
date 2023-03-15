from django import forms 

class MakeNewNote(forms.Form):
	text = forms.CharField(label="", widget=forms.Textarea, max_length = 10000)
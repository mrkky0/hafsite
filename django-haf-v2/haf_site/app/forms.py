from django import forms

class SearchForm(forms.Form):
    arama_terimi = forms.CharField(max_length=100, required=False)

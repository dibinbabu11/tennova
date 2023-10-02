from dataclasses import field, fields
from django import forms
from . models import Recipie
class recipie_form(forms.ModelForm):
    class Meta:
        model=Recipie
        fields=['name','prep_time','difficulty','Image','vegetarian']
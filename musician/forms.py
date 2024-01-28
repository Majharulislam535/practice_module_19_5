from django import forms
from .import models

class Musician(forms.ModelForm):
    class Meta:
        model = models.Musicians_Model
        fields='__all__'
from django import forms
from .models import Torneo

class Liguilla(forms.ModelForm):
  class Meta:
    model = Torneo
    fields = "__all__"
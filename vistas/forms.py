from django import forms
from .models import Torneo,Equipo

class Liguilla(forms.ModelForm):
  class Meta:
    model = Torneo
    themes = forms.ModelMultipleChoiceField(queryset= Torneo.objects ,  to_field_name="type_journement", widget=forms.CheckboxSelectMultiple(), required=False )
    fields = "__all__"
    
class Equipos(forms.ModelForm):
  class Meta:
    model = Equipo
    fields = "__all__"
    
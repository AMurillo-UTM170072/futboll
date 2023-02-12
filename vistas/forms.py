from django import forms
from .models import Torneo

class Liguilla(forms.ModelForm):
  class Meta:
    model = Torneo
    themes = forms.ModelMultipleChoiceField(queryset= Torneo.objects ,  to_field_name="type_journement", widget=forms.CheckboxSelectMultiple(), required=False )
    fields = "__all__"
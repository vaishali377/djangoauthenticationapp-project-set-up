from django import forms
from django.forms import ModelForm
from .models import ProjectMaster

class ProjectMasterForm(ModelForm):
    class Meta:
        model=ProjectMaster
        fields=('user','project_name',)



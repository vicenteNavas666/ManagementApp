from django import forms
from .models import Projects

class ProjectForm(forms.ModelForm):                                                             #form model for Project creation form
    class Meta:                                                                                 #define metadata of parent class 'ModelForm'
        model = Projects                                                                        #database model
        fields = ['Title', 'Description', 'StartDate', 'EndDate', 'Status', 'Priority']

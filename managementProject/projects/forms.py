from django import forms
from .models import Projects, Tasks

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['Title', 'Description', 'StartDate', 'EndDate', 'Status', 'Priority']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("StartDate")
        end_date = cleaned_data.get("EndDate")

        if end_date and start_date:
            if end_date < start_date:
                raise forms.ValidationError("End Date must be greater than or equal to Start Date.")

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['Title', 'Description', 'StartDate', 'EndDate']

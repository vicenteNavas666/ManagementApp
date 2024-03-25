from django import forms
from .models import Projects, Tasks

class ProjectForm(forms.ModelForm):
    Title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'block w-full bg-FormGray text-white h-12 rounded-md my-1',
            'placeholder': 'Title'
        })
    )

    Description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full text-white bg-FormGray h-full my-1 rounded-md',
            'rows': '5',
            'placeholder': 'Description'
        })
    )

    StartDate = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'w-full bg-FormGray text-white h-12 rounded-md my-1',
            'placeholder': 'Start Date',
            'type': 'date'  # Asegura que el tipo de entrada sea 'date' para compatibilidad con HTML5
        })
    )

    EndDate = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'w-full bg-FormGray text-white h-12 rounded-md my-1',
            'placeholder': 'End Date',
            'type': 'date'
        })
    )

    Status = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-FormGray text-white h-12 rounded-md my-1',
            'placeholder': 'Status'
        })
    )

    Priority = forms.ChoiceField(
        choices=[
            ('LOW', 'Low'),
            ('MEDIUM', 'Medium'),
            ('HIGH', 'High')
        ],
        widget=forms.Select(attrs={
            'class': 'w-full bg-FormGray text-white h-12 rounded-md my-1',
            'placeholder': 'Priority'
        })
    )

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

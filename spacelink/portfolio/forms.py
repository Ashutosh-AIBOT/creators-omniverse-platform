from django import forms
from .models import Portfolio, Project


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'name',
            'headline',
            'email',
            'phone',
            'bio',
            'about',
            'theme',
            'is_public'
        ]
        widgets = {
            'about': forms.Textarea(attrs={'rows': 5}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'link', 'image']

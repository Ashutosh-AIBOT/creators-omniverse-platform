from django import forms
from testprofiles.models import Profile, LinkItem

class ProfileForm(forms.ModelForm):
    # To allow entering multiple skills and currently working roles as newline-separated strings
    skills = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Add your skills, one per line (e.g., Matplotlib, Sklearn, Pandas)'
        }),
        help_text="Enter your skills separated by new lines."
    )
    currently_working = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'What are you currently doing? One per line (e.g., Data Scientist, Data Analyst)'
        }),
        help_text="Enter your current roles or activities separated by new lines."
    )

    class Meta:
        model = Profile
        fields = ['bio', 'about', 'phone_number', 'is_public', 'skills', 'currently_working']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write something about yourself...'}),
            'about': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us more about yourself...'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'is_public': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Initialize skills and currently_working fields with newline joined strings if they exist
        if self.instance and self.instance.pk:
            self.fields['skills'].initial = "\n".join(self.instance.get_skills_list())
            self.fields['currently_working'].initial = "\n".join(self.instance.get_currently_list())

    def save(self, commit=True):
        profile = super().save(commit=False)

        # Save the model first to have a primary key if new
        if commit:
            profile.save()

        # Process skills: save as a single string in the DB (comma separated) or however you store it
        skills_str = self.cleaned_data.get('skills', '')
        profile.skills = skills_str  # Assuming your model has a field named `skills` (CharField or TextField)
        
        currently_str = self.cleaned_data.get('currently_working', '')
        profile.currently = currently_str  # Assuming your model has a field named `currently`

        if commit:
            profile.save()
        return profile


class LinkItemForm(forms.ModelForm):
    class Meta:
        model = LinkItem
        fields = ['section', 'title', 'description', 'button_text', 'url', 'is_public']
        widgets = {
            'section': forms.TextInput(attrs={'placeholder': 'Section name (e.g. Projects, Social)'}),
            'title': forms.TextInput(attrs={'placeholder': 'Name of the link'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Description of the link'}),
            'button_text': forms.TextInput(attrs={'placeholder': 'Button text (e.g. Visit, Go)'}),
            'url': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
            'is_public': forms.CheckboxInput(),
        }


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['resume_url', 'resume_is_public']
        widgets = {
            'resume_url': forms.URLInput(attrs={
                'placeholder': 'https://drive.google.com/...',
                'class': 'input-url'
            }),
            'resume_is_public': forms.CheckboxInput(attrs={'class': 'checkbox'}),
        }

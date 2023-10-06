# journey/forms.py
from django import forms
from .models import Milestone

class MilestoneTagForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['tags']

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['title', 'parent']

from django import forms
from .models import Milestone

class MilestoneCustomizationForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Add tags'}),
        help_text='Separate tags with commas'
    )

    class Meta:
        model = Milestone
        fields = ['title', 'description']

    def clean_tags(self):
        tags = self.cleaned_data['tags']
        # Process and validate tags if needed
        return tags.split(',')

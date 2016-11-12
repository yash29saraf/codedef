from django import forms
from models import Knowledge,Topics
from django.forms.widgets import CheckboxSelectMultiple

YEAR = (  
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)
TOPICS = (  
    ('Searching', 'Searching'),
    ('Sorting', 'Sorting'),
    ('DP', 'DP'),
)

class KnowledgeForm(forms.ModelForm):
    language=forms.BooleanField(required=False,label="Knows atleast one Programming Language")
    workshop=forms.BooleanField(required=False,label="Workshop on the Basics is required")
    year=forms.ChoiceField(choices=YEAR)
    topics=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),required=False,queryset=Topics.objects.all())
    
    
    
    class Meta:
		model = Knowledge
		fields='__all__'

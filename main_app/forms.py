from django import forms
from .models import Comments, Movie


class CommentForm(forms.ModelForm):
    # meta configuration variable for your class
    # this is just the way django has defined it
    class Meta:
        model = Comments
        fields = ['comment', 'date', 'movie', 'user']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }
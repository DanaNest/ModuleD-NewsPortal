from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(
        min_length=20,
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 60})
    )
    title = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'cols': 60})
    )

    class Meta:
        model = Post
        fields = [
            'post_category',
            'author',
            'title',
            'text',
        ]
        labels = {
            'post_category': 'Category',
        }

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        title = cleaned_data.get('title')

        if title == text:
            raise ValidationError('Название и текст не должны совпадать')

        return cleaned_data

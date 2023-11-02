import django_filters
from django import forms

from .models import Post, Category


class PostFilter(django_filters.FilterSet):
    data_creation = django_filters.DateFilter(
        field_name='data_creation',
        label='Позже чем:',
        lookup_expr='gt',
        widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'},
                                       format='%Y-%m-%dT%H:%M',)
    )
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название',

    )
    category = django_filters.ModelChoiceFilter(
        field_name='category',
        label='Категория',
        queryset=Category.objects.all(),
        empty_label='Любая'
    )

    class Meta:
        model = Post
        fields = ['data_creation', 'title', 'category']

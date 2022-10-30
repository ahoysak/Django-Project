from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text_article', 'category', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'forms-post', 'placeholder': 'Назва статті'}),
            'text_article': forms.Textarea(attrs={'class': 'forms-post', 'placeholder': 'Текст статті'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'forms-post'}),
            'author': forms.TextInput(attrs={'class': 'forms-post', 'value': '', 'id': 'elder', 'type': 'hidden'})
        }

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class PassForm(forms.Form):
    email = forms.CharField(required=True)
    username = forms.CharField(required=True)

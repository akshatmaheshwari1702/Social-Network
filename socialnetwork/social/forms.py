from django import forms
from django.forms import fields
from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"rows": "3", "placeholder": "Say Something....."}),
    )

    class Meta:
        model = Post
        fields = ["body"]

from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id' : "usercomment",
        'placeholder' : "Type your comment",
        'rows': '3'
    }))
    class Meta:
        model = Comment
        fields = ('content', )
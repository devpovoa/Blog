from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Comentário',
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Digite seu comentário...'
            })
        }
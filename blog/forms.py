from django import forms

from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('pen_name','title', 'text','rating',)

class CommentForm(forms.ModelForm):


	class Meta:
		model = Comment
		fields = ('pen_name','text',) 
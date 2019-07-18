from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['mission_number','title','content','description']
        #writer, mission_number 삭제예정
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['mission_number','title','content','urlcontent','description']
        #writer, mission_number 삭제예정

    widgets = {
        'title':forms.TextInput(
            attrs = {
                'class':'form-control',
            }
        ),
        'content':forms.FileInput(
            attrs = {
                'class':'form-control',
            }
        ),
        'urlcontent':forms.TextInput(
            attrs = {
                'class':'form-control',
            }
        ),
        'description':forms.TextInput(
            attrs = {
                'class':'form-control',
            }
        )
    }
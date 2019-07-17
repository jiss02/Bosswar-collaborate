from django.shortcuts import render,get_object_or_404
from post.models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'mission/index.html',{'posts':posts})


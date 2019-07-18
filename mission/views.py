from django.shortcuts import render,get_object_or_404
from post.models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'mission/index.html',{'posts':posts})

def new(request):
    return render(request, 'mission/new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'mission/new.html', {'form': form})

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.delete()
    return redirect('index')



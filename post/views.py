from django.shortcuts import render,get_object_or_404,redirect
from .forms import PostForm
from .models import Post
# Create your views here.

def new(request):
    return render(request,'post/new.html')

def detail(request,post_id):
    post_detail = get_object_or_404(Post,pk = post_id)
    return render(request, 'post/detail.html', {'post':post_detail})

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request,'post/new.html',{'form':form})

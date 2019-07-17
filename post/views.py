from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import auth
from .forms import PostForm
from .models import Post
from mission.models import Mission
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
            #포스트 생성시간<= 마감시간 추가예정
            post = form.save(commit = False)
            post.save()
            return redirect('index')
            '''
                else:
                    return render(request, 'mission/index.html', {"Mission_end": '이미 마감된 미션입니다.'})
            '''
    else:
        form = PostForm()
        return render(request,'post/new.html',{'form':form})

def postdelete(request,post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.delete()
    return redirect('index')
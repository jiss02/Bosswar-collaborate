from django.shortcuts import render,get_object_or_404,redirect, HttpResponseRedirect
from django.contrib import auth
from .forms import PostForm
from .models import Post
from profiles.models import Profile
from mission.models import Mission
from post.models import PostVote
import datetime


# Create your views here.

def new(request):
    return render(request,'post/new.html')

def detail(request,post_id):
    post_detail = get_object_or_404(Post,pk = post_id)
    vote = PostVote.objects.filter(user=request.user, post=post_detail)
    return render(request, 'post/detail.html', {'post':post_detail, 'vote':vote})

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST) 
        user = Profile.objects.get(user_id=request.user.id)
        if user.point < 500:
            return render(request, 'mission/index.html', {"Mission_end": '포인트가 부족합니다.'})
        else:
            user.point -= 500
        user.save()
        if form.is_valid():
            post = form.save(commit = False)
            mission_object = Mission.objects.get(mission_number=1)
            now = datetime.datetime.now()
            if now <= mission_object.end_at:
                post.writer = request.user
                post.save()
                return redirect('index')
            else:
                return render(request, 'mission/index.html', {"Mission_end": '이미 마감된 미션입니다.'}) 
    else:
        form = PostForm()
        return render(request,'post/new.html',{'form':form})

def postdelete(request,post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.delete()
    return redirect('index')
    
def postvote(request, post_id):
    user = Profile.objects.get(user_id=request.user.id)
    post = get_object_or_404(Post, pk=post_id)
    voted = PostVote.objects.filter(user=request.user, post=post)
    if not voted:
        votes = user.votes
        if user.votes <= 0:
            user.votes = 0
            user.save()
            return redirect('detail', post_id=post.id)
        else:
            user.votes = votes-1
            user.save() 
            vote = PostVote.objects.create(user=request.user, post=post)
    else:
        voted.delete()
        user.votes += 1
        user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
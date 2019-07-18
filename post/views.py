from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import auth
from .forms import PostForm
from .models import Post
from profiles.models import Profile
from mission.models import Mission
import datetime
import pytz
# Create your views here.

def new(request):
    return render(request,'post/new.html')

def detail(request,post_id):
    post_detail = get_object_or_404(Post,pk = post_id)
    return render(request, 'post/detail.html', {'post':post_detail})

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
    

       
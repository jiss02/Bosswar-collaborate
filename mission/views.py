from django.shortcuts import render,get_object_or_404
from .models import Mission
from .forms import MissionForm
from post.models import Post
import datetime
from django.core.paginator import Paginator
########### 포스트 띄우기 ############

def index(request): 
    posts_all = Post.objects.all().order_by('-id')
    paginator = Paginator(posts_all, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    mission = Mission.objects.filter(start_at__lt = datetime.datetime.now()).filter(end_at__gt = datetime.datetime.now()).all()
    return render(request, 'mission/index.html',{'posts':posts,'posts_all':posts_all,'mission':mission})

############# 미션 관련 ##############

def new(request):
    return render(request, 'mission/new.html')

def missioncreate(request):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.save()
            return redirect('index')
    else:
        form = MissionForm()
        return render(request, 'mission/new.html', {'form': form})

def missionupdate():
        return any

def missiondelete(request, post_id):
    mission = get_object_or_404(Post, pk = post_id)
    mission.delete()
    return redirect('index')

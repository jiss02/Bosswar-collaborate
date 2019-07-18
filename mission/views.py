from django.shortcuts import render,get_object_or_404
from .models import Mission
from .forms import MissionForm
from post.models import Post

########### 포스트 띄우기 ############

def index(request):
    posts = Post.objects.all()
    return render(request, 'mission/index.html',{'posts':posts})

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

def missiondelete(request, post_id):
    mission = get_object_or_404(Post, pk = post_id)
    mission.delete()
    return redirect('index')



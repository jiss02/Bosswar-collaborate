from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
import mission.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_detail/<int:first_id>'mission.views.first_detail, name='first_detail'),
    # path('<int:post_id>/', mission.views.show, name='show'),
    path('new/', mission.views.new, name='new'),
    path('missioncreate/', mission.views.missioncreate, name='missioncreate'),
    path('missiondelete/<int:post_id>', mission.views.missiondelete, name='missiondelete'),
    path('firstperson/'mission.views.firstperson, name='firstperson')
]

from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
import mission.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('<int:post_id>/', mission.views.show, name='show'),
    path('new/', mission.views.new, name='new'),
    path('missioncreate/', mission.views.missioncreate, name='missioncreate'),
    path('missiondelete/<int:post_id>', mission.views.missiondelete, name='missiondelete'),
]

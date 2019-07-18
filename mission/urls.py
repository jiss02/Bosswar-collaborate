from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
import mission.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mission.views.index, name='index'),
    path('mission/<int:post_id>', mission.views.show, name='show'),
    path('mission/new', mission.views.new, name='new'),
    path('mission/postcreate', mission.views.postcreate, name='postcreate'),
    path('crud/postdelete/<int:post_id>', mission.views.postdelete, name='postdelete'),
]

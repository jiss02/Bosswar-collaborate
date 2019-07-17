from django.urls import path
from . import views

urlpatterns = [
    path('new/',views.new, name='new'),
    path('detail/<int:post_id>',views.detail, name='detail'),
    path('postcreate/',views.postcreate,name='postcreate'),
    path('postdelete/<int:post_id>',views.postdelete, name='postdelete')
]

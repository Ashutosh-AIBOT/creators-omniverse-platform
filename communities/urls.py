from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('explore/', views.explore_communities, name='explore'),
    path('join/', views.join_group, name='join_group'),
    path('leave/<int:group_id>/', views.leave_group, name='leave_group'),
    path('delete/<int:group_id>/', views.delete_group, name='delete_group'),
    path('ignore/<int:group_id>/', views.ignore_group, name='ignore_group'),
    path('topic/<int:topic_id>/', views.community_topic, name='topic_detail'),
    path('topic/<int:topic_id>/create/', views.create_group, name='create_group'),
    path('chat/<int:group_id>/', views.chat_room, name='chat_room'),
]

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Topic, CommunityGroup, Message
from django.http import HttpResponseForbidden

@login_required
def explore_communities(request):
    topics = Topic.objects.all()
    return render(request, 'communities/explore.html', {'topics': topics})

@login_required
def community_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    # Filter out groups ignored by the current user
    groups = topic.groups.exclude(ignored_by=request.user)
    return render(request, 'communities/topic_detail.html', {'topic': topic, 'groups': groups})

@login_required
def create_group(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        privacy = request.POST.get('privacy')
        password = request.POST.get('password', '')
        description = request.POST.get('description', '')
        
        group = CommunityGroup.objects.create(
            topic=topic,
            name=name,
            creator=request.user,
            privacy=privacy,
            password=password if privacy == 'private' else None,
            description=description
        )
        group.members.add(request.user)
        return redirect('communities:chat_room', group_id=group.id)
    
    return render(request, 'communities/create_group.html', {'topic': topic})

@login_required
def join_group(request):
    if request.method == 'POST':
        unique_id = request.POST.get('unique_id', '').upper()
        password = request.POST.get('password', '')
        
        try:
            group = CommunityGroup.objects.get(unique_id=unique_id)
            if group.privacy == 'private' and group.password != password:
                messages.error(request, "Invalid password for this private group.")
                return redirect('communities:explore')
            
            group.members.add(request.user)
            # Remove from ignored list if they decided to join
            group.ignored_by.remove(request.user)
            messages.success(request, f"Joined {group.name}!")
            return redirect('communities:chat_room', group_id=group.id)
            
        except CommunityGroup.DoesNotExist:
            messages.error(request, "Group ID not found.")
    return redirect('communities:explore')

@login_required
def leave_group(request, group_id):
    group = get_object_or_404(CommunityGroup, id=group_id)
    group.members.remove(request.user)
    messages.success(request, f"You left {group.name}.")
    return redirect('communities:explore')

@login_required
def delete_group(request, group_id):
    group = get_object_or_404(CommunityGroup, id=group_id)
    # Only creator or admin can delete
    if request.user == group.creator or request.user.is_superuser:
        group.delete()
        messages.success(request, "Community deleted successfully.")
        return redirect('communities:explore')
    return HttpResponseForbidden("You don't have permission to delete this group.")

@login_required
def ignore_group(request, group_id):
    group = get_object_or_404(CommunityGroup, id=group_id)
    group.ignored_by.add(request.user)
    messages.success(request, f"Group '{group.name}' hidden from your view.")
    return redirect('communities:topic_detail', topic_id=group.topic.id)

@login_required
def chat_room(request, group_id):
    group = get_object_or_404(CommunityGroup, id=group_id)
    if not group.members.filter(id=request.user.id).exists():
        messages.warning(request, "You must join the group to view messages.")
        return redirect('communities:topic_detail', topic_id=group.topic.id)
        
    chat_messages = group.messages.all()[:50]
    return render(request, 'communities/chat_room.html', {'group': group, 'chat_messages': chat_messages})

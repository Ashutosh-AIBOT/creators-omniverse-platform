from django.urls import path
from . import views

app_name = "testprofiles"

urlpatterns = [
    # View a user's profile/dashboard
    path('profile/<str:username>/', views.profile_view, name='profile'),

    # Edit the logged-in user's profile info
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    # Add a new item/link to a specific section of the profile/dashboard
    path('add-item/<str:section>/', views.add_item, name='add_item'),

    # Edit an existing item/link by its primary key
    path('edit-item/<int:pk>/', views.edit_item, name='edit_item'),

    # Delete an item/link by its primary key
    path('delete-item/<int:pk>/', views.delete_item, name='delete_item'),

    # Toggle the visibility (public/private) of an item/link
    path('toggle-item-visibility/<int:pk>/', views.toggle_item_visibility, name='toggle_item_visibility'),
    
    
    path('resume/', views.add_or_update_resume, name='add_resume'),


]

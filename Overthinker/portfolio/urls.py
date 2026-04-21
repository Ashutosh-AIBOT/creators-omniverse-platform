from django.urls import path
from .views import edit_portfolio, view_portfolio, add_project

app_name = 'portfolio'

urlpatterns = [
    path('edit/', edit_portfolio, name='edit_portfolio'),
    path('project/add/', add_project, name='add_project'),
    path('<str:username>/', view_portfolio, name='view_portfolio'),
]

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('auth_with/', views.auth_with, name='auth_with'),
    path('logout/', views.logout, name='logout'),
    path('profile_edit/', views.editPage, name='profile_edit'),
    path('profile/<str:pk>/', views.profile, name = 'profile'),
    path('profile_lists/', views.profiles_list, name='profiles_list')
]

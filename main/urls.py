from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('features/', views.features, name='features'),
    path('confession_matching/', views.confession_matching, name='confession_matching'),
    path('compatibility_suggestions/', views.compatibility_suggestions, name='compatibility_suggestions'),
    path('location_suggestions/', views.location_suggestions, name='location_suggestions'),
    path('profile/', views.profile_view, name='profile_view'),
    path('confession_matching/', views.confession_matching, name='confession_matching'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
]
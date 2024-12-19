from django.contrib import admin 
from django.urls import path
from newapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('' , views.home , name='home'),
    path( path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')),
    path('signup' , views.signup , name='signup'),
    path('ManagerSignup' , views.ManagerSignup , name='ManagerSignup'),
    path('tournament' , views.tournament , name='tournament'),
    path('Contact' , views.Contact , name='Contact'),
    path('Viewteams', views.Viewteams, name='Viewteams'),
    path('game', views.game, name='game'),
    path('home' , views.home , name = 'home'),
    
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
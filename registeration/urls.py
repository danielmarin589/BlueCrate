from django.urls import path
from registeration.views import LoginView, RegisterView, LogoutView ,ProfileView
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'registeration'
urlpatterns = [
	path('', LoginView.as_view(), name = 'login'),
	path('register', RegisterView.as_view(), name = 'register'),
	path('logout',LogoutView.as_view(),name ='logout'),
    path('profile',  ProfileView.as_view(), name = 'profile'),
]

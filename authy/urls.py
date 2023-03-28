from django.urls import path
from .views import EditProfile,register , signin,logout
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    # Profile Section
    path('profile/edit', EditProfile, name="editprofile"),

    # User Authentication
    path('sign-up/', register, name="sign-up"),
    path('sign-in/', signin, name='sign-in'),
    path('sign-out/' , logout , name= "sign-out"), 
]

from django.urls import path
from .views import login_view, register_view, logout_view, delete_profile
from django.urls import path
from .views import UserProfileView, EditProfileView



urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit-profile'),
    path('profile/excluir/', delete_profile, name='delete-profile'),
]
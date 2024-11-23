from django.urls import path
from .views import login_view, UserCreateView, logout_view, delete_profile, UserProfileView, EditProfileView
from django.urls import path

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('editar-perfil/', EditProfileView.as_view(), name='edit-profile'),
    path('profile/excluir/', delete_profile, name='delete-profile'),
]
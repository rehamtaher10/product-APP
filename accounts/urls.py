from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import ShowProfile,  CreateCustomUser, EditProfile, DeleteProfile


urlpatterns = [
  path('',include('django.contrib.auth.urls')),
  path('profile/', login_required(ShowProfile.as_view()), name='accounts.profile'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('register', CreateCustomUser.as_view(), name='accounts.create'),
  path('<int:pk>/edit', login_required(EditProfile.as_view()), name='profile.edit'),
  path('<int:pk>/delete', login_required(DeleteProfile.as_view()), name='profile.delete')
]
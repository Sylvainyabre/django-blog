from django.urls import path
from . import views as api_views


app_name = "auth"
urlpatterns = [
    path('users/<pk>/', api_views.UserDetailView.as_view(),
         name='user_detail'),
    path('profiles/<pk>/', api_views.ProfileDetailView.as_view(),
         name='profile_detail'),

]

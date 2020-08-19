from django.urls import path
from django.contrib import admin
from . import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('registration/register/', accounts_views.register, name='register'),
    path('registration/login/', accounts_views.user_login, name='login'),
    path('account/logout/', accounts_views.logout, name='logout'),
    path('registration/profile/', accounts_views.profile, name='profile'),
    path('registration/profile/update/', accounts_views.profile_update, name='profile_update'),
    path('registration/password-reset/',auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html'),
         name='password_reset'),
    path('registration/reset/',auth_views.PasswordResetDoneView.as_view(
        template_name = 'registration/password_reset_form.html'),
         name='password_reset'),
    path('registration/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
         template_name = 'registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('registration/reset/complete/',auth_views.PasswordResetCompleteView.as_view(
         template_name = 'registration/password_reset_done.html'),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

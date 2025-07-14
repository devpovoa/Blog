from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from accounts.views.user_auth_views import UserRegisterView, CustomPasswordResetView
from accounts.views.profile_update_view import ProfileUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/auth/logged_out.html'), name='logout'),
    path('register/', UserRegisterView.as_view(template_name='accounts/auth/register.html'), name='register'),
    path('perfil/', ProfileUpdateView.as_view(template_name='accounts/profile/profile_update.html'),
         name='profile_update'),
    path('senha/resetar/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('senha/resetar/enviado/',
         PasswordResetDoneView.as_view(template_name='accounts/password/password_reset_done.html'),
         name='password_reset_done'),
    path('senha/resetar/confirmar/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('senha/resetar/completo/',
         PasswordResetCompleteView.as_view(template_name='accounts/password/password_reset_complete.html'),
         name='password_reset_complete'),
]

from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from accounts.forms.user_register_form import UserRegisterForm
from django.contrib.auth.views import PasswordResetView


class UserRegisterView(FormView):
    template_name = 'accounts/auth/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('profile_update')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password/password_reset.html'
    email_template_name = 'accounts/password/password_reset_email.txt'
    html_email_template_name = 'accounts/password/password_reset_email.html'
    subject_template_name = 'accounts/password/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

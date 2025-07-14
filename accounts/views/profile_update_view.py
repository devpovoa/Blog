from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models.profile import Profile
from accounts.forms.profile_form import ProfileForm
from blog.models import Comment
from django.urls import reverse_lazy


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile_update')  # ou 'post_list' se preferir

    def get_object(self, queryset=None):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['comments'] = Comment.objects.filter(user=user, active_at=True).order_by('-created_at')
        return context

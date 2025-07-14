from django.views.generic import DetailView, FormView
from django.shortcuts import redirect
from django.urls import reverse
from blog.models import Post
from blog.forms import CommentForm


class PostDetailView(FormView, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active_at=True).order_by('-created_at')
        return context

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={self.request.path}")
        comment = form.save(commit=False)
        comment.post = self.get_object()
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Evita que anônimos submetam comentários e causem erro de validação."""
        kwargs = super().get_form_kwargs()
        if not self.request.user.is_authenticated and self.request.method == "POST":
            kwargs['data'] = None  # limpa o POST se for anônimo
        return kwargs

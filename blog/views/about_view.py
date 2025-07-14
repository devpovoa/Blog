from django.views.generic import TemplateView
from blog.models.about import About


class AboutView(TemplateView):
    template_name = 'pages/sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context

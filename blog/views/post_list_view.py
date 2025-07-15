from django.views.generic import ListView
from blog.models import Post, Category
from django.db.models import Q


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_at']
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Post.objects.all().order_by('-published_at')
        category_slug = self.request.GET.get('category')

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(slug__icontains=query))
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['categories'] = Category.objects.all()
        context['current_category'] = self.request.GET.get('category')
        return context

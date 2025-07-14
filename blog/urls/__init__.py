from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls.post_urls')),
    path('', include('blog.urls.page_urls')),
]


from django.urls import path
from blog.views.contact_view import ContactView
from blog.views.about_view import AboutView

urlpatterns = [
    path('sobre/', AboutView.as_view(), name='sobre'),
    path('contato/', ContactView.as_view(), name='contato'),
]

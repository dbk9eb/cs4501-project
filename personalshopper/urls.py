from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'users/([\w.@+-]+)/$', views.user),
    url(r'ps/([\w.@+-]+)/$', views.ps),
    url(r'items/([\w.@+-]+)/$', views.item),
]

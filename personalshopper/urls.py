from django.conf.urls import url
from . import views

urlpatterns = [
    # create must come first or regex will assume 'create' is name
    url(r'users/create/$', views.create_user),
    url(r'ps/create/$', views.create_ps),
    url(r'items/create/$', views.create_item),
    
    url(r'users/([\w.@+-]+)/$', views.user),
    url(r'ps/([\w.@+-]+)/$', views.ps),
    url(r'items/([\w.@+-]+)/$', views.item),
]

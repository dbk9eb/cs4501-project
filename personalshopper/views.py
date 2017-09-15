from django.shortcuts import render, get_object_or_404
from django.core import serializers

from .models import User, PersonalShopper, Item

def user(request, us):
    _user = get_object_or_404(User, username=us)
    json = serializers.serialize('json', [_user])
    return render(request, 'personalshopper/api.html', {"json": json})

def ps(request, us):
    _user = get_object_or_404(PersonalShopper, username=us)
    json = serializers.serialize('json', [_user])
    return render(request, 'personalshopper/api.html', {"json": json})

def item(request, n):
    _item = get_object_or_404(Item, name=n)
    json = serializers.serialize('json', [_item])
    return render(request, 'personalshopper/api.html', {"json": json})

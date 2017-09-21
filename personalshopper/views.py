from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.core.exceptions import FieldDoesNotExist
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import User, PersonalShopper, Item

@csrf_exempt
def user(request, us):
    
    _user = get_object_or_404(User, username=us)

    # Update from POST data if it exists
    updatePOST(request.POST, _user)

    # Return in JSON format
    #checkUser = User.objects.get(pk=3)
    #return HttpResponse(checkUser.username)
    return returnJSON(request, _user)

@csrf_exempt
def ps(request, us):
    _user = get_object_or_404(PersonalShopper, username=us)

    # Update from POST data
    updatePOST(request.POST, _user)
        
    return returnJSON(request, _user)

@csrf_exempt
def item(request, n):
    _item = get_object_or_404(Item, name=n)

    # Update from POST data
    updatePOST(request.POST, _item)

    return returnJSON(request, _item)

def updatePOST(post, model):
    for key in post:
        try:
            model._meta.get_field(key)
        except Exception:
            continue
        else:
            setattr(model, key, post[key])
    model.save()

@csrf_exempt
def create_user(request):

    # Checking if POST data exists
    if request.method != 'POST':
        return HttpResponse("Must send POST data to create a User.")

    # Check that no unrecognized keys are loaded
    # Set recognized keys in User
    user = User(email="", password="", country="", username="")
    for key in request.POST:
        try:
            user._meta.get_field(key)
        except FieldDoesNotExist:
            return HttpResponse("Field '" + key + "' not in User. No object created")
        else:
            setattr(user, key, request.POST[key])

    # If any fields are missing, do not proceed
    if user.email == "" or user.password == "" or user.country == "" or user.username == "":
        return HttpResponse("Not all required fields provided. Please specificy username, password, email and country.")

    try:
        user.save()
    except IntegrityError as e:
        return HttpResponse("Raised error: " + str(e) + ". No object created.")
    
    return returnJSON(request, user)

@csrf_exempt
def create_ps(request):
    # Checking if POST data exists
    if request.method != 'POST':
        return HttpResponse("Must send POST data to create a PersonalShopper.")

    # Check that no unrecognized keys are loaded
    # Set recognized keys in User
    ps = PersonalShopper(email="", password="", country="", username="")
    for key in request.POST:
        try:
            ps._meta.get_field(key)
        except FieldDoesNotExist:
            return HttpResponse("Field '" + key + "' not in PersonalShopper. No object created.")
        else:
            setattr(ps, key, request.POST[key])

    # If any fields are missing, do not proceed
    if ps.email == "" or ps.password == "" or ps.country == "" or ps.username == "":
        return HttpResponse("Not all required fields provided. Please specificy username, password, email and country.")

    try:
        ps.save()
    except IntegrityError as e:
        return HttpResponse("Raised error: " + str(e) + ". No object created.")
    return returnJSON(request, ps)

@csrf_exempt
def create_item(request):
    
    # Checking if POST data exists
    if request.method != 'POST':
        return HttpResponse("Must send POST data to create an Item.")

    # Check that no unrecognized keys are loaded
    # Set recognized keys in User
    item = Item(price = 0, name="", description="", country="")
    for key in request.POST:
        try:
            user._meta.get_field(key)
        except FieldDoesNotExist:
            return HttpResponse("Field '" + key + "' not in Item. No object created.")
        else:
            setattr(item, key, request.POST[key])

    # If any fields are missing, do not proceed
    if item.name == "" or item.country == "":
        return HttpResponse("Not all required fields provided. Please specificy item name and country.")
    if item.price < 0:
        return HttpResponse("Price cannot be negative. No object created.")

    try:
        item.save()
    except IntegrityError as e:
        return HttpResponse("Raised error: " + str(e) + ". No object created.")
    return returnJSON(request, item)

def returnJSON(request, model):
    json = serializers.serialize('json', [model])
    return render(request, 'personalshopper/api.html', {"json": json})

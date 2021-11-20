from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from PictureManager.models import Location, Picture
from django.views.decorators.csrf import csrf_exempt
import json 

# simple Home Page
def home(request):
    print("hello")
    return HttpResponse("welcome to the home page")

# location CRUD
@csrf_exempt
def locations(request):
    #gets all locations
    if request.method == 'GET':
        locations = list(Location.objects.values())
        return JsonResponse(locations, safe=False)
    
    #add a location to the DB
    if request.method == 'POST':
        #convert the body into a Dict
        body = json.loads(request.body.decode("utf-8"))
        #new location entry with the form data passed in as values(***Try to find a way to simplfy this)
        newLocation = Location(name=body["name"],country=body["country"],caption=body["caption"],continent=body["continent"])
        newLocation.save()
        print("newLocation")
        return HttpResponse("adding location")


# Picture Crud
def pictures(request,location):
    #gets all pictures related to a location
    if request.method == 'GET':
        #attains the correct location from the DB
        location = Location.objects.get(name=location)
        #all pictures related to the location
        pictures = location.picture_set.all()
        pictures = list(pictures.values())
        return JsonResponse(pictures, safe=False)


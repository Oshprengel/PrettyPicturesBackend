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
def locations(request,location=None):
    #converts body into a python dict 
    body = json.loads(request.body.decode("utf-8"))
    #gets all locations
    if request.method == 'GET':
        #if a particular locations photos are requested
        if(location):
            #attains the correct location from the DB
            location = Location.objects.get(name=location)
            #all pictures related to the location
            pictures = location.picture_set.all()
            pictures = list(pictures.values())
            return JsonResponse(pictures, safe=False)
        #otherwise send back all locations
        else:
            locations = list(Location.objects.values())
            return JsonResponse(locations, safe=False)
    
    #add a location to the DB
    if request.method == 'POST':
        #new location entry with the form data passed in as values(***Try to find a way to simplfy this)
        newLocation = Location(name=body["name"],country=body["country"],caption=body["caption"],continent=body["continent"])
        newLocation.save()
        print("newLocation")
        return HttpResponse("added location")

    #updates a locations details
    if request.method == 'PUT':
        #the location we will be updating 
        location = Location.objects.get(id=body["id"])
        #update location attributes and save
        location.name = body["name"]
        location.country = body["country"]
        location.continent = body["continent"]
        location.caption = body["caption"]
        location.save()
        
        return HttpResponse("updated location")

    #deletes a location
    if request.method == 'DELETE':
        #the location we will be deleting
        location=Location.objects.get(id=body["id"])
        location.delete()
        return HttpResponse("location deleted")
# pictures CRUD
@csrf_exempt
def pictures(request):
    #converts the body into a python dict
    if (request.body):
      body = json.loads(request.body.decode('utf-8'))
    #creates a new photo ****REFACTOR THIS TO USE ID INSTEAD OF LOCATION NAME
    if request.method == "POST":
        #finds the id of the location which the user is trying to add the picture to
        location_id = Location.objects.get(name=body["location"]).id
        #creates and saves the new picture
        picture = Picture(link=body["link"], location_id=location_id, caption=body["caption"])
        picture.save()
        return HttpResponse("added picture")
    
    #updates a photos caption
    if request.method =="PUT":
        #the picture that we will be updating
        picture = Picture.objects.get(id=body["id"])
        #updates the caption then saves
        picture.caption = body["caption"]
        picture.save()
        return HttpResponse("updated picture")

    #deletes a photo from the db
    if request.method =="DELETE":
        picture = Picture.objects.get(id=body["id"])
        picture.delete()
        return HttpResponse("deleted picture")




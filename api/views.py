from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer

from .models import Item
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Item List": "/list/",
        "Item Search": "/search/<str:name>/",
        "Add Item": "/add/",
        "Delete Item by exact match": "/delete-exact-match/<str:name>/",
        "Delete Item by partial match": "/delete-partial-match/<str:name>/",
    }
    return Response(api_urls)

@api_view(['GET'])
def itemList(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)
    

# @api_view(['GET'])
# def itemSearch(request, name):
#     #this searches exact matching name
#     items = Item.objects.filter(name=name)
#     serializer = ItemSerializer(items, many=True)

#     return Response(serializer.data)


@api_view(['GET'])
def itemSearch(request, name):
    # this searches exact matching name
    items = Item.objects.filter(name=name)

    # increment the search count for the items
    for item in items:
        item.search_count += 1
        item.save()

    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteExactMatchItem(request, name):
    item = Item.objects.filter(name=name)
    item.delete()
    return Response("Item Deleted")

@api_view(['DELETE'])
def deletePartialMatchItem(request, name):
    item = Item.objects.filter(name__contains=name)
    item.delete()
    return Response("Item Deleted")

@api_view(['GET'])
def index(request):
    return render(request, 'api/index.html')



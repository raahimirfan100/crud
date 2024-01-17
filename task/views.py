from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError

import logging
logger = logging.getLogger(__name__)


class ItemViewSet(viewsets.ViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=False, methods=['GET'])
    def apiOverview(self, request):
        api_urls = {
            "Item List": "/list/",
            "Item Search": "/search/<str:name>/",
            "Add Item": "/add/",
            "Delete Item by exact match": "/delete-exact-match/<str:name>/",
            "Delete Item by partial match": "/delete-partial-match/<str:name>/",
        }
        return Response(api_urls)

    @action(detail=False, methods=['GET'])
    def itemList(self, request):
        try:
            items = Item.objects.all().order_by('-search_count')
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            logger.error("Failed to retrieve items")
            return Response({"error": "Failed to retrieve items"}, status=500)

    @action(detail=True, methods=['GET'])
    def itemSearch(self, request, name=None):
        try:
            item = self.get_object()
            item.search_count += 1
            item.save()
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Http404 as e:
            logger.error(f"Item {name} not found: {e}")
            return Response({"error": str(e)}, status=404)

    @action(detail=False, methods=['POST'])
    def addItem(self, request):
        serializer = ItemSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except ValidationError as e:
            logger.error(f"Invalid data: {e}")
            print(serializer.errors)
            return Response({"error": str(e)}, status=400)

    @action(detail=False, methods=['DELETE'])
    def deleteItem(self, request, name):
        items = Item.objects.filter(name__contains=name)
        items.delete()
        return Response("Items Deleted")

    def get_object(self):
        queryset = Item.objects.all()
        try:
            obj = queryset.get(name=self.kwargs['name'])
            self.check_object_permissions(self.request, obj)
        except Item.DoesNotExist:
            raise Http404("No item matches the given query.")
        return obj

    @action(detail=False, methods=['GET'])
    def index(self, request):
        return render(request, 'api/index.html')


logging.basicConfig(level=logging.DEBUG)
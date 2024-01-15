from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('list/', itemList, name="item-list"),
    path('search/<str:name>/', itemSearch, name="item-search"),
    path('add/', addItem, name="item-create"),
    path('delete-exact-match/<str:name>/', deleteExactMatchItem, name="item-delete-exact-match"),
    path('delete-partial-match/<str:name>/', deletePartialMatchItem, name="item-delete-partial-match"),
    
    path('index/', index, name='index'),
]
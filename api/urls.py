from django.urls import path
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    #path('', apiOverview, name="api-overview"),
    path('list/', itemList, name="item-list"),
    path('search/<str:name>/', itemSearch, name="item-search"),
    path('add/', addItem, name="item-create"),
    path('delete-exact-match/<str:name>/', deleteExactMatchItem, name="item-delete-exact-match"),
    path('delete-partial-match/<str:name>/', deletePartialMatchItem, name="item-delete-partial-match"),
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    #path('index/', index, name='index'),
]
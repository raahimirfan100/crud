from django.urls import path
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    #path('', apiOverview, name="api-overview"),
    path('list/', ItemViewSet.as_view({'get': 'itemList'}), name="item-list"),
    path('search/<str:name>/', ItemViewSet.as_view({'get': 'itemSearch'}), name="item-search"),
    path('add/', ItemViewSet.as_view({'post': 'addItem'}), name="add-item"),
    path('delete/<str:name>/', ItemViewSet.as_view({'delete': 'deleteItem'}), name="delete-item"),
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    #path('index/', index, name='index'),
]
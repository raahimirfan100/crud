from django.urls import path
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', apiOverview, name="api-overview"),
    path('list/', ItemViewSet.as_view({'get': 'itemList'}), name="item-list"),
    path('search/<str:name>/', ItemViewSet.as_view({'get': 'itemSearch'}), name="item-search"),
    path('add/', ItemViewSet.as_view({'post': 'addItem'}), name="add-item"),
    path('delete/<str:name>/', ItemViewSet.as_view({'delete': 'deleteItem'}), name="delete-item"),
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    
    #path('index/', index, name='index'),
]
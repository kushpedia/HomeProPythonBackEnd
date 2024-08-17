from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CategoryViewSet, ServiceViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('profiles.urls')),
	path('api/', include(router.urls)),
]

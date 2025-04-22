from rest_framework import routers
from .views import PostViewSet, ImageViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r"^image", ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

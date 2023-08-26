from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ColorPaletteViewSet, ColorViewSet

router = DefaultRouter()
router.register(r'colorpalettes', ColorPaletteViewSet)
router.register(r'colors', ColorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

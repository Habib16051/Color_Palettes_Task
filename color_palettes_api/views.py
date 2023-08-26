from rest_framework import viewsets, permissions
from .models import ColorPalette, Color
from .serializers import ColorPaletteSerializer, ColorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from reversion.models import Version
from reversion import revisions as reversion

class ColorPaletteViewSet(viewsets.ModelViewSet):
    queryset = ColorPalette.objects.all()
    serializer_class = ColorPaletteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'dominant_colors__value', 'accent_colors__value']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        dominant_colors_data = self.request.data.get('dominant_colors')
        accent_colors_data = self.request.data.get('accent_colors')

        if dominant_colors_data is not None:
            instance.dominant_colors.clear()
            for color_data in dominant_colors_data:
                Color.objects.create(role='dominant', palette=instance, **color_data)

        if accent_colors_data is not None:
            instance.accent_colors.clear()
            for color_data in accent_colors_data:
                Color.objects.create(role='accent', palette=instance, **color_data)

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        palette = self.get_object()
        user = request.user

        if palette.favorites.filter(user=user).exists():
            palette.favorites.remove(user)
            message = "Removed from favorites."
        else:
            palette.favorites.add(user)
            message = "Added to favorites."

        return Response({"message": message})

    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        palette = self.get_object()
        versions = Version.objects.get_for_object(palette)
        serialized_versions = [{'version_id': version.id, 'revision': version.revision.date_created} for version in versions]
        return Response(serialized_versions)

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

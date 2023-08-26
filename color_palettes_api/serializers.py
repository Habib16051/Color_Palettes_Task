from rest_framework import serializers
from .models import ColorPalette, Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class ColorPaletteSerializer(serializers.ModelSerializer):
    dominant_colors = ColorSerializer(many=True, read_only=True)
    accent_colors = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = ColorPalette
        fields = '__all__'

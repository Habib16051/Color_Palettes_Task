from django.db import models
from django.conf import settings
from reversion import revisions as reversion

class Color(models.Model):
    value = models.CharField(max_length=20)  # Store color in HEX format
    role = models.CharField(max_length=20)  # Store 'dominant' or 'accent'
    color_palette = models.ForeignKey('ColorPalette', on_delete=models.CASCADE)

    def __str__(self):
        return self.value

@reversion.register
class ColorPalette(models.Model):
    name = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dominant_colors = models.ManyToManyField('Color', related_name='dominant_palettes')
    accent_colors = models.ManyToManyField('Color', related_name='accent_palettes')

    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_palettes', blank=True)

    def __str__(self):
        return self.name

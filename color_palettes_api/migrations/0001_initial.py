# Generated by Django 4.2.4 on 2023-08-25 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=7)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ColorPalette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_public', models.BooleanField(default=True)),
                ('accent_colors', models.ManyToManyField(related_name='accent_palettes', to='color_palettes_api.color')),
                ('dominant_colors', models.ManyToManyField(related_name='dominant_palettes', to='color_palettes_api.color')),
                ('favorites', models.ManyToManyField(blank=True, related_name='favorite_palettes', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='color',
            name='color_palette',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='color_palettes_api.colorpalette'),
        ),
    ]
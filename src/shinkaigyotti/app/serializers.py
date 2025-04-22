from rest_framework import serializers
from .models import Post, ImageModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'photo')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ("id", "image", "matched_fish_url")
        read_only_fields = ('matched_fish_url', "id")

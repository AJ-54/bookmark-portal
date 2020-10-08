from rest_framework import serializers
from .models import *

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['my_id', 'link', 'title', 'publisher', 'tags', 'created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    bookmark = BookmarkSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['my_id', 'title', 'created_at', 'updated_at', 'bookmark']
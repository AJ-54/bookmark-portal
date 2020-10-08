from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import routers, serializers, viewsets, status
from .models import Bookmark,Tag
from .serializers import BookmarkSerializer,TagSerializer

# Create your views here.

class BookmarkViewSet(viewsets.ModelViewSet):
    """
    List all Bookmarks, or create a new bookmark.
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    List all Tags, or create a new Tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    ordering_fields = ['updated_at']

class BookMarkListAPIView(ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    
class BookMarkCreateAPIView(CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookMarkDeleteAPIView(DestroyAPIView):
    lookup_field = "link"
    serializer_class = BookmarkSerializer

    def get_queryset(self, **kwargs):
        queryset = Bookmark.objects.filter(link = self.kwargs["link"])
        return queryset

class BookMarkUpdateAPIView(UpdateAPIView):
    lookup_field = "link"
    serializer_class = BookmarkSerializer

    def get_queryset(self, **kwargs):
        queryset = Bookmark.objects.filter(link = self.kwargs["link"])
        return queryset


class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TagCreateAPIView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDeleteAPIView(DestroyAPIView):
    lookup_field = "title"
    serializer_class = TagSerializer

    def get_queryset(self, **kwargs):
        queryset = Tag.objects.filter(title = self.kwargs["title"])
        return queryset
    
    
    

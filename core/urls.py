from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^api/bookmarks$',BookMarkListAPIView.as_view(), name="all_bks"),
    url(r'^api/bookmarks/create$',BookMarkCreateAPIView.as_view(), name="create_bk"),
    url(r'^api/bookmarks/update/(?P<link>.+)$',BookMarkUpdateAPIView.as_view(), name="update_bk"),
    url(r'^api/bookmarks/delete/(?P<link>.+)$',BookMarkDeleteAPIView.as_view(), name="delete_bk"),
    url(r'^api/tags$',TagListAPIView.as_view(), name="all_bks"),
    url(r'^api/tags/create$',TagCreateAPIView.as_view(), name="create_tag"),
    url(r'^api/tags/delete/(?P<title>.+)$',TagDeleteAPIView.as_view(), name="delete_tag"),
    
]
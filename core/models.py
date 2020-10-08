from django.db import models
import uuid
import datetime
import os

# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
class Bookmark(TimeStampMixin):
    
    my_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    tags = models.ManyToManyField("Tag", related_name = "bookmark", blank=True)

    def __str__(self):
        return self.title

class Tag(TimeStampMixin):

    my_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    
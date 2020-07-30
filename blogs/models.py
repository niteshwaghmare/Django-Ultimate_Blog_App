from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from markdown import markdown
import readtime
# Create your models here.

STATUS = ((0, "Draft"), (1, "Publish"))


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.FileField(upload_to='blog_images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    
    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))

    def get_read_time(self):
        return readtime.of_text(self.content)
    
    def __str__(self):
        return self.title

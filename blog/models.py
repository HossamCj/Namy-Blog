from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.text import slugify

from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    category = models.ForeignKey(Category, related_name='post_category', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)  # Call the real save method

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
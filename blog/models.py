from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author', verbose_name=_('author'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=120)
    slug = models.SlugField(max_length=120, null=True, blank=True, verbose_name=_('url'))
    description = models.TextField(_('description'), max_length=500, blank=True,)
    image = models.ImageField(_('image'), upload_to='post/')
    created_at = models.DateTimeField(_('created_at'), default=timezone.now)
    tags = TaggableManager()
    category = models.ForeignKey(Category, related_name='post_category', verbose_name=_('category'), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)  # Call the real save method

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
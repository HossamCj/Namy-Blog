from django.db import models


class Settings(models.Model):
    site_name = models.CharField(max_length=120)
    description = models.TextField(max_length=5000)
    address = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='settings/')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    fb_link = models.URLField(max_length=200)
    tw_link = models.URLField(max_length=200)
    insta_link = models.URLField(max_length=200)

    def __str__(self):
        return self.site_name
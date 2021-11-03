from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Place(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120)
    icons = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Property(models.Model):
    author = models.ForeignKey(User, related_name='property_author', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=5000)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='property/')
    place = models.ForeignKey(Place, related_name='property_place', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='property_category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)  # call the real save method

    def get_absolute_url(self):
        return reverse('property_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    def check_availability(self):
        all_reservations = self.book_property.all()
        now = timezone.now().date()

        for reservation in all_reservations:
            if now > reservation.date_to:
                return 'Available'
            elif reservation.date_from < now < reservation.date_to:
                booked_to = reservation.date_to
                return f'Booked to : {booked_to}'
        else:
            return 'Available'

    def get_average_rate(self):
        all_reviews = self.review_property.all()
        all_ratings = 0

        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rate
            return round(all_ratings / len(all_reviews), 2)
        else:
            return '-'


class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propertyimages/')

    def __str__(self):
        return str(self.property)


class PropertyReview(models.Model):
    author = models.ForeignKey(User, related_name='review_author', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='review_property', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.property)


NUMBERS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)


class PropertyBook(models.Model):
    user = models.ForeignKey(User, related_name='book_owner', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='book_property', on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    guest_numbers = models.PositiveIntegerField(choices=NUMBERS)
    children_numbers = models.PositiveIntegerField(choices=NUMBERS)

    def __str__(self):
        return str(self.property)

    def booked(self):
        now = timezone.now().date()
        return self.date_from < now < self.date_to

    booked.boolean = True
















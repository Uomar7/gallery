from django.db import models
import datetime as dt
    
class category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

class Location(models.Model):
    location_name = models.CharField(max_length = 40)
    
    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    posted_by = models.CharField(max_length = 40)
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(category)
    location = models.ForeignKey(Location, default=1)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['posted_by']
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def todays_images(cls):
        today = dt.datetime.today()
        images = cls.objects.filter(posted__date=today)
        return images

    @classmethod
    def days_images(cls,date):
        images = cls.objects.filter(posted__date=date)
        return images
    
    @classmethod
    def search_by_posted(cls,search_term):
        images = cls.objects.filter(posted_by__icontains = search_term)
        return images
    
    @classmethod
    def search_by_location(cls, search_term):
        images = cls.objects.filter(location__icontains=search_term)
        return images
    
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images
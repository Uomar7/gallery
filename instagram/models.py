from django.db import models

class Image(models.Model):
    posted_by = models.CharField(max_length = 40)
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['posted_by']
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

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
    image = models.ForeignKey(Image)
    category = models.ManyToManyField(category)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

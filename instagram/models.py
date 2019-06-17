from django.db import models

class Image(models.Model):
    name = models.CharField(max_length = 40)
    description = models.TextField()
    email = models.EmailField()
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['name']

class category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    location_name = models.CharField(max_length = 40)
    image = models.ForeignKey(Image)
    category = models.ManyToManyField(category)

    def __str__(self):
        return self.location_name
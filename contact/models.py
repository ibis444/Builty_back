from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Bio(models.Model):
    name = models.CharField(max_length=255) 
    position = models.CharField(max_length=255)   
    address = models.TextField() 
    telephone = models.CharField(max_length=20)  
    fax = models.CharField(max_length=20, blank=True, null=True)  
    email = models.EmailField()  

    def __str__(self):
        return self.name


class FAQ(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Map(models.Model):
    map_src = models.URLField()

    def __str__(self):
        return f"Map - {self.id}"


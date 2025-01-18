from django.db import models
from django.core.exceptions import ValidationError

class Services(models.Model):
    title = models.CharField(max_length=255)  # Başlıq
    description = models.TextField()         # Təsvir
    breadcrumb_title = models.CharField(max_length=255,) 
    breadcrumb_home = models.CharField(max_length=255, )      
    background_image = models.ImageField(upload_to='backgrounds_service/', )  

    class Meta:
        verbose_name = "(Service seifesi 1 )"  
        verbose_name_plural = "(Service seifesi 1)"  

    def __str__(self):
        return self.title

class ServiceIcon(models.Model):
    title = models.CharField(max_length=255)  # Xidmətin başlığı
    description = models.TextField()  # Xidmətin təsviri
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)  # Şəkil (isteğe bağlı)
    class Meta:
        verbose_name = "(Service seifesi 2 )"  
        verbose_name_plural = "(Service seifesi 2)" 
    def __str__(self):
        return self.title

class Counter(models.Model):
    number = models.PositiveIntegerField()
    suffix = models.CharField(max_length=10, blank=True, null=True)  
    label = models.CharField(max_length=100)  
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "(Service seifesi 3  )"  
        verbose_name_plural = "(Service seifesi 3)" 

    def __str__(self):
        return self.description


class VideoPopup(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='video-popup-images/')
    video_file = models.FileField(upload_to='video-popup-videos/')  # MP4 video faylı

    def __str__(self):
        return self.title


class Offering(models.Model):
    title = models.CharField(max_length=255)  # Xidmətin adı
    description = models.TextField()          # Təsvir
    image = models.ImageField(upload_to='offerings/')  # Şəkil

    def __str__(self):
        return self.title


class Footer(models.Model):
    information_text = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Footer Data"

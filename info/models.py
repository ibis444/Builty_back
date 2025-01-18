# models.py
from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='slider_images/')

    def __str__(self):
        return self.title



class HomeService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)  # Şəkil sahəsi

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_one = models.ImageField(upload_to='about_images/', blank=True, null=True)
    image_two = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.title

from django.db import models

class Counter(models.Model):
    number = models.PositiveIntegerField()
    suffix = models.CharField(max_length=10, blank=True, null=True)  
    label = models.CharField(max_length=100)  
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


from django.db import models

class CoreFeature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    num = models.PositiveIntegerField()  
    
    def __str__(self):
        return self.title


class CoreFeatureVideo(models.Model):
    video_file = models.FileField(upload_to='videos/')  
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True) 

    def __str__(self):
        return f"Video {self.id}"

class CoreFeatureSection(models.Model):
    title = models.CharField(max_length=255) 
    subtitle = models.CharField(max_length=255)  

    def __str__(self):
        return self.title



class RenovationInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='background_images/')
    circle_image = models.ImageField(upload_to='circle_images/')

    def __str__(self):
        return self.title

class ClientReview(models.Model):
    section_header = models.CharField(max_length=255,)
    reviews_header = models.CharField(max_length=255,)
    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    review = models.TextField()
    image = models.ImageField(upload_to='client_review_images/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name}"


# ++++++++++++++++++++++ABOUT+++++++++++++++++++++++++++++++

class AboutUs(models.Model):
    title = models.CharField(max_length=255)  # Başlıq
    description = models.TextField()         # Təsvir
    breadcrumb_title = models.CharField(max_length=255, default="About Us") 
    breadcrumb_home = models.CharField(max_length=255, default="Home")      
    background_image = models.ImageField(upload_to='backgrounds/', default='backgrounds/default.png')  

    class Meta:
        verbose_name = "About (About seifesi 1 )"  
        verbose_name_plural = "About (About seifesi 1)"  

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    main_heading = models.CharField(max_length=255)
    who_we_are_text = models.TextField()
    who_we_are_image = models.ImageField(upload_to='about_images/')
    whats_in_it_for_me_title = models.CharField(max_length=255)
    whats_in_it_for_me_points = models.JSONField()  
    whats_in_it_for_me_image = models.ImageField(upload_to='about_images/')
    
    def __str__(self):
        return self.main_heading

    class Meta:
        verbose_name = "About seifesi 2"
        verbose_name_plural = "About seifesi 2"


class HowItWorks(models.Model):
    background_image = models.ImageField(upload_to='how_it_works/', blank=True, null=True)  # Background şəkli
    heading_text = models.CharField(max_length=255, default="Plan + Control")  # Başlıq üçün alt yazı
    heading_title = models.CharField(max_length=255, default="How it Works")  # Başlıq mətn

    step_1_title = models.CharField(max_length=255, default="Phase Plan")
    step_1_description = models.TextField(default="This step connects the design process and its milestones with construction.")

    step_2_title = models.CharField(max_length=255, default="Design Pull Plan")
    step_2_description = models.TextField(default="We work with the design team to establish a detailed plan for reaching our goals.")

    step_3_title = models.CharField(max_length=255, default="Coordinated Layout")
    step_3_description = models.TextField(default="This process creates a single point of truth: drawings all project.")

    step_4_title = models.CharField(max_length=255, default="Quality Control")
    step_4_description = models.TextField(default="Having geometry worked out in the Layout step, prior to construction.")

    

    class Meta:
        verbose_name = "About seifesi 3"
        verbose_name_plural = "About seifesi 3"

    def __str__(self):
        return "How It Works Settings"






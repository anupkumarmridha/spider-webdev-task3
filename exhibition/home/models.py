from decimal import Decimal
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True, blank=True,upload_to='images/profile/')
    website_url=models.CharField(max_length=255,null=True, blank=True)
    facebook_url=models.CharField(max_length=255,null=True, blank=True)
    twitter_url=models.CharField(max_length=255,null=True, blank=True)
    instagram_url=models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return str(self.user)
    

class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("homeView")

class Product(models.Model):
    title=models.CharField(max_length=255)
    product_image=models.ImageField(null=True, blank=True,upload_to='images/')
    title_tag=models.CharField(max_length=255)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    desc=RichTextField(blank=True, null=True)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    category=models.CharField(max_length=255)
    likes=models.ManyToManyField(User,related_name='product_posts')

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()

    
        
    def __str__(self):
        return self.title + '|' + str( self.author)

    def get_absolute_url(self):
        return reverse('homeView')

class Comment(models.Model):
    product=models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    parrent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Bid(models.Model):
    product=models.ForeignKey(Product, related_name="bids", on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price=models.DecimalField(max_digits=8, decimal_places=2)
    parrent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

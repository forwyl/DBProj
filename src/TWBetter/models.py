# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import default


# Create your models here.
class Producer(models.Model):
    key = models.AutoField(primary_key=True)
    number = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100, null=True)
    manager = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=300, null=True)
    phone = models.CharField(max_length=100, null=True)
    fax = models.CharField(max_length=100, null=True)
    type = models.IntegerField(null=True)
    website = models.URLField(blank=True)
    
    def _str_(self):
        return self.name

class GFood(models.Model):
    key = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, null=True)
    agrospec = models.CharField(max_length=10, null=True)
    catalogs_id = models.CharField(max_length=20, null=True)
    county = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=50, null=True)
    image_url = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    spc_catalogs_id = models.CharField(max_length=50, null=True)
    title = models.TextField(blank=True, null=True)
    unit_price = models.TextField(blank=True, null=True)
    modify_date = models.CharField(max_length=100, null=True)
    producer = models.ForeignKey(Producer, null=True, default = None)
    
    def _str_(self):
        return self.id
    
class UserProfile(models.Model):
    user_background = models.OneToOneField(User)
    user_nickname = models.CharField(max_length=200, default="鄉民")
    user_image = models.ImageField(upload_to="pics/", default="pics/default.png")
    user_membership = models.BooleanField(default = False)
 
    def _str_(self):
        return self.user_nickname
     
class Comment(models.Model):
    key = models.AutoField(primary_key=True)
    message = models.TextField(blank=True, null=True)
    ranking = models.IntegerField(default=0)
    user_profile = models.ForeignKey(UserProfile)
    gfood = models.ForeignKey(GFood)
 
    def _str_(self):
        return self.key
 
class Favorite(models.Model):
    key = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile)
    gfood = models.ForeignKey(GFood)
     
    def _str_(self):
        return self.key
    
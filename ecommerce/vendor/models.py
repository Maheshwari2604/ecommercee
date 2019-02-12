# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from Loma.models import md
from Loma.models import Loma_master, md
from django.db import models
from products.models import product

# Create your models here.
class vendor_master(models.Model):
    Vendor_name = models.CharField(max_length=120)
    Vendor_Address = models.CharField(max_length=120)
    Vendor_mandi_name = models.ForeignKey(md, blank=True)
    loma_id = models.ForeignKey(Loma_master)
    loma_name = models.CharField(max_length=120)
    loma_zone = models.CharField(max_length=120)
    username = models.CharField(max_length=120, unique = True)
    password = models.CharField(max_length=120)
    vendor_mobile_no = models.IntegerField(default = 0.00)

    #description = models.TextField(null=False)
    #price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)
    vendor_slug = models.SlugField(unique = True)
    #Image = models.FileField(upload_to='products/images/', null= True)   
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return "Username: %s, Zone: %s" %(self.username, self.loma_zone)

#model jaha vendors aaakr apne apne price daaalenge.......
#than ye price loma ke pass jaaayenge jaha show honge.....
class vendor_daily_PL(models.Model):
    vendor = models.ForeignKey(vendor_master)
    loma_id = models.ForeignKey(Loma_master)
    Mandi_name = models.ForeignKey(md)
    product = models.ForeignKey(product)
    product_name = models.CharField(max_length=120, blank=True)
    offer_price = models.FloatField(null=False)
    list_price = models.IntegerField(null=False)
    qty = models.IntegerField(null=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 'Product name: %s, username and zone are : %s' %(self.product_name,self.vendor)


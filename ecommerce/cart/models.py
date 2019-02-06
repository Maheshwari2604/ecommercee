# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products.models import product, product_Image, product_price
from django.db import models
from user_model.models import register_model

# Create your models here.

class subT(models.Manager):
    def subtotal(self):
        price = self.quantity * self.subtotal
        print price
        return self.price


class cartitem(models.Model):
    #cart = models.ForeignKey('Carttotal', null=True, blank=True)
    user_id = models.ForeignKey(register_model)
    product = models.ForeignKey(product, null=True, blank=True)
    productImage = models.ForeignKey(product_Image, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(default=19.99, max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    sub = subT()


    def __unicode__(self):
        return str(self.user_id)


class carttotal(models.Model):
    user_id = models.ForeignKey(register_model)
    cart = models.ForeignKey('cartitem', null=True, blank=True)
    Total = models.FloatField(default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.user_id)


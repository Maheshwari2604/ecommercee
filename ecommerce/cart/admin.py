# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import cartitem,  carttotal
from django.contrib import admin

# Register your models here.
class CartItem(admin.ModelAdmin):
    list_display = ['product','quantity', 'price', 'updated']
    search_fields = ['product']
    readonly_fields = ['timestamp', 'updated']


admin.site.register(cartitem, CartItem)


class CartItem(admin.ModelAdmin):
    list_display = ['cart', 'Total', 'updated']
    search_fields = ['cart']
    readonly_fields = ['timestamp', 'updated']

admin.site.register(carttotal, CartItem)
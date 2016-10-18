# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from .models import Category, Poll


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = 'name', 'author', 'category'

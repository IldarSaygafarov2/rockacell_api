from django.contrib import admin
from django.db import models
from modeltranslation.admin import TranslationAdmin
from unfold import admin as unfold_admin
from unfold.contrib.forms.widgets import WysiwygWidget

from .models import Category, Post, Product, Request


@admin.register(Request)
class RequestAdmin(unfold_admin.ModelAdmin):
    list_display = ["id", "fullname", "phone", "email", "company"]


@admin.register(Category)
class CategoryAdmin(unfold_admin.ModelAdmin, TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Product)
class ProductAdmin(unfold_admin.ModelAdmin, TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }


@admin.register(Post)
class PostAdmin(unfold_admin.ModelAdmin, TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }

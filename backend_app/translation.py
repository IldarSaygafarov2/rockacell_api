from modeltranslation.translator import translator, TranslationOptions

from .models import Category, Product, Post


class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "short_description", "description")


class CategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


class PostTranslationOptions(TranslationOptions):
    fields = ("title", "short_description", "full_description")


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Post, PostTranslationOptions)

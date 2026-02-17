from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from core import settings

from .models import Category, Post, Product, Request
from .schemas import (
    CategorySchema,
    PostDetailSchema,
    PostListSchema,
    ProductSchema,
    RequestInSchema,
    RequestOutSchema,
)

api = NinjaAPI()


@api.get("/categories/", response=list[CategorySchema])
def get_categories(request: HttpRequest):
    return Category.objects.all()


@api.get("/products/", response=list[ProductSchema])
def get_products(request: HttpRequest):
    return Product.objects.all()


@api.get("/posts/", response=list[PostListSchema])
def get_posts(request: HttpRequest):
    posts = Post.objects.all()
    return posts


@api.get("/posts/{id}/", response=PostDetailSchema)
def get_post_by_id(request: HttpRequest, id: int):
    post = get_object_or_404(Post, pk=id)
    other_posts = Post.objects.all().exclude(pk=post.id)
    result = PostDetailSchema(
        id=post.id,
        title=post.title,
        full_description=post.full_description,
        photo_1=post.photo_1.url if post.photo_1 else None,
        photo_2=post.photo_2.url if post.photo_2 else None,
        posts=other_posts,
    )
    return result


from django.core.mail import send_mail


@api.post("/request/create/", response=RequestOutSchema)
def create_request(request: HttpRequest, body: RequestInSchema):
    data = body.model_dump()
    new_request = Request.objects.create(**data)
    send_mail(
        subject="Тема письма",
        message="тест",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[data["email"]],
        fail_silently=False,
    )
    return new_request

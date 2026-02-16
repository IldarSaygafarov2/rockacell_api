from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from .models import Category, Post, Product, Request
from .schemas import CategorySchema, ProductSchema, PostDetailSchema, PostListSchema, RequestOutSchema, RequestInSchema

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


@api.post('/request/create/', response=RequestOutSchema)
def create_request(request: HttpRequest, body: RequestInSchema):
    return Request.objects.create(**body.model_dump())

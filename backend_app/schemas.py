from ninja import Schema


class CategorySchema(Schema):
    id: int
    title: str
    slug: str


class ProductSchema(Schema):
    id: int
    title: str
    description: str
    preview: str
    category: CategorySchema


class PostListSchema(Schema):
    id: int
    title: str
    slug: str
    preview: str
    short_description: str


class PostDetailSchema(Schema):
    id: int
    title: str
    full_description: str
    photo_1: str | None = None
    photo_2: str | None = None
    posts: list[PostListSchema]

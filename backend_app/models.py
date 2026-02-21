from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="Слаг")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=150)
    slug = models.SlugField(verbose_name="Слаг", max_length=150)
    short_description = models.TextField(verbose_name="Краткое описание", default="")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(verbose_name="Фото", upload_to="products/photos/")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="categories",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Post(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=150)
    slug = models.SlugField(verbose_name="Слаг", max_length=150)
    preview = models.ImageField(upload_to="posts/photos/", verbose_name="Фото")
    short_description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(verbose_name="Полное описание")
    photo_1 = models.ImageField(
        verbose_name="Первое фото в описании",
        upload_to="posts/photos/",
        null=True,
        blank=True,
    )
    photo_2 = models.ImageField(
        verbose_name="Второе фото в описании",
        upload_to="posts/photos/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Request(BaseModel):
    fullname = models.CharField(verbose_name="Полное имя", max_length=150)
    phone = models.CharField(verbose_name="Номер телефона", max_length=20)
    email = models.EmailField(verbose_name="Почта")
    company = models.CharField(verbose_name="Компания")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Запрос пользователя"
        verbose_name_plural = "Запросы пользователей"

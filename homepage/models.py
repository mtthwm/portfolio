from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField

# Create your models here.
class User(AbstractUser):
    pass

class BlogPostManager(models.Manager):
    def unpublished (self):
        return self.get_queryset().filter(published=False)

    def published (self):
        return self.get_queryset().filter(published=True)

class PostTag (models.Model):
    title = models.CharField(max_length=50, null=False)
    color = ColorField(default='#0099cc')
    text_color = ColorField(default='#000000')

    def __str__(self):
        return f"{self.title}"

class BlogPost(models.Model):
    title = models.CharField(max_length=250, null=False)
    title_slug = models.SlugField(primary_key=True, unique=True, max_length=50)
    date_published = models.DateField()
    content = RichTextUploadingField()
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(PostTag)

    objects = BlogPostManager()

    def __str__(self):
        return f"{self.title}"

class PortfolioProject(models.Model):
    title = models.CharField(max_length=250, null=False)
    title_slug = models.SlugField(primary_key=True, unique=True, max_length=50)
    description = RichTextUploadingField()
    ongoing = models.BooleanField(default=False)
    main_image = models.ImageField(upload_to='public/portfolioimages')
    associated_posts = models.ManyToManyField(BlogPost)
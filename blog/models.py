import datetime as dt
from django.db import models
from django.urls import reverse
from blog.utils import slugify_instance_title

from conf import settings
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils import timezone
# Create your models here.

# User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import User

class Post(models.Model):
    
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now_add=True, null=False)


    @property
    def name(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"post_slug": self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # do another something

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Post)


def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Post)
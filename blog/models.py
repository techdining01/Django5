from django.db import models
from django.conf import settings
from django.utils import timezone



class PublishedManager(models.Manager):
    def get_queryset(self):
        super().get_queryset().filter(status=Post.Status.PUBLISHED)



class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = ('DR', 'Draft')
        PUBLISHED = ('PD', 'Published')

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_post'
        )
    status = models.CharField(
        max_length=2, choices=Status,
        default=Status.DRAFT
        )
    body = models.TextField()
    publish = models.DateTimeField(timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(
                fields=['-publish'])
                ]
    
    def __str__ (self):
        return self.title

    


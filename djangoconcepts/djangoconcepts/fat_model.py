from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(User, related_name='posts')
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)

    @property
    def is_published(self):
        from django.utils import timezone
        return self.publish_date < timezone.now()

    def get_absolute_url(self):
        return reverse('blog-post', args=self.slug)

    def pre_save(self, instance, add):
        from django.utils.text import slugify
        if not instance.slug:
            instance.slug = slugify(self.title)


class BlogComment(models.Model):
    blog_post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, related_name='comments')
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)

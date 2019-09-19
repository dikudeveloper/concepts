from django.db import models
from .behaviors import Authorable, Permalinkable, Timestampable, Publishable


class BlogPost(Authorable, Permalinkable, Timestampable, Publishable, models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    url_name = "blog-post"

    @property
    def slug_source(self):
        return self.title


class BlogComment(Authorable, Permalinkable, Timestampable, Publishable, models.Model):
    blog_post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments')

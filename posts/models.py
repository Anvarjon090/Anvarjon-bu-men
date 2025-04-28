from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    views_count = models.PositiveIntegerField(default=0)  # <<< TO‘G‘RILANDI
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Model<{self.title}>"

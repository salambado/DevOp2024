
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    # thumbnail = models.ImageField(null=True, blank=True, upload_to="img", default="placeholder.png")
    # img_alt = models.CharField(max_length=200, null=True, blank=True)
    body = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)
    # featured = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    demo = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.headline
    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count =+ 1
                slug = slugify(self.headline) + '' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
from django.db import models
from ckeditor.fields import RichTextField
from users.models import CustomUser
from django.urls import reverse
from PIL import Image

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="cover_images/%Y/%m/%d", blank=True)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})

from django.db import models
from django.urls import reverse
from dataclasses import dataclass
# Create your models here.

class Article(models.Model):

    title = models.CharField( max_length=50)
    content = models.TextField(max_length=100)
    

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})

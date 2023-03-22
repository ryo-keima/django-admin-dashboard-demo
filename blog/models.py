from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User


class Blog(models.Model):
    title = models.CharField(
        verbose_name=_("title"),
        max_length=50,
        blank=False,
        null=False)
    body = models.TextField(
        verbose_name=_("body"),
        blank=True,
        null=True)
    author = models.ForeignKey(
        User,
        verbose_name=_("author"),
        on_delete=models.CASCADE)
    slug = models.SlugField(
        verbose_name=_("slug"),
        unique=True)
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name=_("updateded_at"),
        auto_now=True
    )
